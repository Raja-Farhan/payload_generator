import base64
def encode(payload):
    return base64.b64encode(payload.encode()).decode()
