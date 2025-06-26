def encode(payload):
    return ''.join(f'\\x{ord(c):02x}' for c in payload)
