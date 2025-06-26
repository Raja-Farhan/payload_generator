import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

def run_gui():
    def update_variants(event):
        atk = attack_type.get()
        variant_dropdown.set("")
        if atk == "xss":
            variant_dropdown['values'] = ["reflected", "stored", "dom", "svg", "nullbyte", "eventhandler", "srcdoc"]
        elif atk == "sqli":
            variant_dropdown['values'] = ["error", "union", "blind"]
        elif atk == "cmdinj":
            variant_dropdown['values'] = ["linux", "windows", "ping"]
        else:
            variant_dropdown['values'] = []

    def generate():
        args = ["python", "main.py"]

        atk = attack_type.get()
        var = variant_dropdown.get()
        if atk: args.extend(["--attack-type", atk])
        if var: args.extend(["--variant", var])
        if encode.get(): args.extend(["--encode", encode.get()])
        if obfuscate.get(): args.extend(["--obfuscate", obfuscate.get()])
        if export_json.get(): args.append("--json")
        if copy_clip.get(): args.append("--copy")
        if fuzz_mode.get(): args.append("--fuzz")

        subprocess.run(args)
        messagebox.showinfo("Success", "Payload(s) generated successfully!")

    root = tk.Tk()
    root.title("Payload Generator Tool")
    root.geometry("400x320")
    root.resizable(False, False)

    ttk.Label(root, text="Attack Type:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
    attack_type = ttk.Combobox(root, values=["xss", "sqli", "cmdinj"])
    attack_type.grid(row=0, column=1)
    attack_type.bind("<<ComboboxSelected>>", update_variants)

    ttk.Label(root, text="Variant:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
    variant_dropdown = ttk.Combobox(root)
    variant_dropdown.grid(row=1, column=1)

    ttk.Label(root, text="Encoding:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
    encode = ttk.Combobox(root, values=["base64", "url", "hex", "unicode", "mix"])
    encode.grid(row=2, column=1)

    ttk.Label(root, text="Obfuscation:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
    obfuscate = ttk.Combobox(root, values=["comments", "spacing"])
    obfuscate.grid(row=3, column=1)

    export_json = tk.BooleanVar()
    copy_clip = tk.BooleanVar()
    fuzz_mode = tk.BooleanVar()

    tk.Checkbutton(root, text="Export JSON", variable=export_json).grid(row=4, column=0, sticky='w', padx=10)
    tk.Checkbutton(root, text="Copy to Clipboard", variable=copy_clip).grid(row=5, column=0, sticky='w', padx=10)
    tk.Checkbutton(root, text="Fuzz Mode (All Variants)", variable=fuzz_mode).grid(row=6, column=0, columnspan=2, padx=10)

    tk.Button(root, text="Generate Payload", command=generate).grid(row=7, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()