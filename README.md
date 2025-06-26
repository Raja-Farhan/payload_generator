# payload_generator_tool/README.md

# Modular Payload Generation Tool 🛡️

A Python-based tool for generating evasion-ready payloads for common web vulnerabilities including **XSS**, **SQL Injection**, and **Command Injection**. Includes encoding, obfuscation, fuzzing, and filter bypass techniques. 

---

## Features

✅ XSS Payload Generator (Reflected, Stored, DOM, SVG, Null Byte, Event Handler, Srcdoc)

✅ SQL Injection Payload Generator (Error-based, Union-based, Blind)

✅ Command Injection Payload Generator (Linux, Windows, Ping variants)

✅ Encoding Options: Base64, URL, Hex, Unicode, Mixed Encoding

✅ Obfuscation Options: Comment Insertion, Spacing Obfuscation

✅ Fuzz Mode: Generate All Payload Variants for Testing

✅ Clipboard Copy Option

✅ Export to JSON File

✅ Simple Tkinter GUI with Dynamic Dropdowns

---

## Installation

```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Usage (CLI)

### Basic Payload Generation
```bash
python main.py --attack-type xss --variant reflected
```

### With Encoding & Obfuscation
```bash
python main.py --attack-type sqli --variant union --encode url --obfuscate comments
```

### Fuzz Mode (Generate All Variants)
```bash
python main.py --attack-type cmdinj --fuzz --encode base64
```

### Clipboard & JSON Export
```bash
python main.py --attack-type xss --variant dom --copy --json
```

---

## Usage (GUI)

```bash
python gui.py
```

- Dynamic dropdowns for Attack Type and Variants
- Optional encoding, obfuscation, copy to clipboard, fuzz mode, JSON export
- Click "Generate Payload" to execute

---

## Project Structure

```
├── main.py                  # CLI Logic
├── gui.py                   # Tkinter GUI
├── cli.py                   # (Entry point placeholder)
├── output_handler.py        # Output formatting & clipboard logic
├── utils.py                 # File operations
├── requirements.txt         # Dependencies
├── README.md                 # This file
│
├── modules/
│   ├── xss.py               # XSS payloads
│   ├── sqli.py              # SQLi payloads
│   └── cmdinj.py            # Command Injection payloads
│
├── encoders/
│   ├── base64_encoder.py
│   ├── url_encoder.py
│   ├── hex_encoder.py
│   ├── unicode_encoder.py
│   └── mix_encoder.py
│
├── obfuscators/
│   ├── comments.py
│   └── spacing.py
```

---

## Requirements

- Python 3.8+
- pyperclip
- urllib3

Install with:
```bash
pip install -r requirements.txt
```

---

## References & Inspiration

- [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [PortSwigger XSS Filter Evasion Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
- [OWASP Command Injection Guide](https://owasp.org/www-community/attacks/Command_Injection)

---

## Future Improvements

- Burp Suite / ZAP API Integration
- More WAF Bypass Techniques
- Real-time Payload Preview in GUI
- Additional Encoding & Obfuscation Modules

---

## Disclaimer

This tool is intended for **ethical testing** and **educational purposes** only. Unauthorized use is prohibited.
