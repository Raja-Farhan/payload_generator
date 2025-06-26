import json
import pyperclip
from utils import save_to_file

def generate_output(payload, args):
    if args.copy:
        pyperclip.copy(payload)
    if args.json:
        save_to_file("payloads.json", json.dumps({"type": args.attack_type, "payload": payload}))
    print("\n[+] Generated Payload:\n", payload)