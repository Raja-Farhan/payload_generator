def generate(variant):
    payloads = {
        "error": "' OR 1=1 --",
        "union": "' UNION SELECT NULL, NULL --",
        "blind": "' AND 1=1 WAITFOR DELAY '0:0:5' --",
    }
    return payloads.get(variant, "' OR 'a'='a")
