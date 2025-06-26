def encode(payload):
    return ''.join(f'\\u{ord(c):04x}' for c in payload)
