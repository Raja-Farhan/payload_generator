import argparse
from modules import xss, sqli, cmdinj
from encoders import base64_encoder, url_encoder, hex_encoder, unicode_encoder, mix_encoder
from obfuscators import comments, spacing
import pyperclip
import json
from output_handler import generate_output

# Map encoder strings to functions
encoders = {
    "base64": base64_encoder.encode,
    "url": url_encoder.encode,
    "hex": hex_encoder.encode,
    "unicode": unicode_encoder.encode,
    "mix": mix_encoder.encode
}

def handle_encoding(payload, encoder_name):
    if encoder_name in encoders:
        return encoders[encoder_name](payload)
    return payload

def handle_obfuscation(payload, obfuscator_name):
    if obfuscator_name == "comments":
        return comments.obfuscate(payload)
    elif obfuscator_name == "spacing":
        return spacing.obfuscate(payload)
    return payload

def main():
    parser = argparse.ArgumentParser(description="Modular Payload Generator Tool")
    parser.add_argument("--attack-type", choices=["xss", "sqli", "cmdinj"], required=True)
    parser.add_argument("--variant", help="Payload variant (e.g., reflected, error-based, linux)")
    parser.add_argument("--encode", choices=encoders.keys())
    parser.add_argument("--obfuscate", choices=["comments", "spacing"])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--copy", action="store_true")
    parser.add_argument("--fuzz", action="store_true", help="Generate multiple fuzzed payloads")
    args = parser.parse_args()

    payloads = []
    if args.fuzz:
        variants = ["reflected", "stored", "dom", "svg"] if args.attack_type == "xss" else \
                   ["error", "union", "blind"] if args.attack_type == "sqli" else \
                   ["linux", "windows", "ping"]
        for variant in variants:
            if args.attack_type == "xss":
                p = xss.generate(variant)
            elif args.attack_type == "sqli":
                p = sqli.generate(variant)
            elif args.attack_type == "cmdinj":
                p = cmdinj.generate(variant)
            if args.obfuscate:
                p = handle_obfuscation(p, args.obfuscate)
            if args.encode:
                p = handle_encoding(p, args.encode)
            payloads.append(p)
    else:
        if args.attack_type == "xss":
            payloads = [xss.generate(args.variant)]
        elif args.attack_type == "sqli":
            payloads = [sqli.generate(args.variant)]
        elif args.attack_type == "cmdinj":
            payloads = [cmdinj.generate(args.variant)]

        if args.obfuscate:
            payloads = [handle_obfuscation(p, args.obfuscate) for p in payloads]
        if args.encode:
            payloads = [handle_encoding(p, args.encode) for p in payloads]

    for p in payloads:
        generate_output(p, args)

if __name__ == "__main__":
    main()
