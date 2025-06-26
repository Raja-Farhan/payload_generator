from encoders import base64_encoder, hex_encoder, unicode_encoder
import random
def encode(payload):
    funcs = [base64_encoder.encode, hex_encoder.encode, unicode_encoder.encode]
    return ''.join(random.choice(funcs)(char) for char in payload)
