import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Key derivation
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Password strength check
def check_strength(password):
    if len(password) < 6:
        return "Weak", "red"
    elif any(c.isdigit() for c in password) and any(c.isalpha() for c in password) and len(password) >= 8:
        return "Strong", "green"
    else:
        return "Medium", "orange"

# Encrypt file
def encrypt_file():
    file = file_path.get()
    pw = password.get()
    if not file or not pw:
        messagebox.showwarning("Missing info", "Select file and enter password")
        return
    try:
        with open(file, "rb") as f:
            data = f.read()
        salt = os.urandom(16)
        key = derive_key(pw, salt)
        encrypted = Fernet(key).encrypt(data)
        with open(file + ".secure", "wb") as f:
            f.write(salt + encrypted)
        messagebox.showinfo("Encrypted", f"Saved: {file}.secure")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Decrypt file
def decrypt_file():
    file = file_path.get()
    pw = password.get()
    if not file or not pw:
        messagebox.showwarning("Missing info", "Select file and enter password")
        return
    try:
        with open(file, "rb") as f:
            content = f.read()
        salt = content[:16]
        data = content[16:]
        key = derive_key(pw, salt)
        decrypted = Fernet(key).decrypt(data)
        out_path = file.replace(".secure", "_decrypted")
        with open(out_path, "wb") as f:
            f.write(decrypted)
        messagebox.showinfo("Decrypted", f"Saved: {out_path}")
    except:
        messagebox.showerror("Error", "Failed. Wrong password or corrupt file.")

# GUI
def update_strength(*_):
    strength, color = check_strength(password.get())
    strength_label.config(text=strength, fg=color)

# --- GUI Layout ---
root = tk.Tk()
root.title("🛡️ File Encryptor")
root.geometry("440x300")
root.resizable(False, False)

file_path = tk.StringVar()
password = tk.StringVar()
password.trace_add("write", update_strength)

tk.Label(root, text="Select file to encrypt/decrypt:", font=("Arial", 11)).pack(pady=10)

file_frame = tk.Frame(root)
file_frame.pack(pady=5)

file_entry = tk.Entry(file_frame, textvariable=file_path, width=40)
file_entry.pack(side="left", padx=5)

browse_btn = tk.Button(file_frame, text="Browse", command=lambda: file_path.set(filedialog.askopenfilename()))
browse_btn.pack(side="right")

tk.Label(root, text="Password:", font=("Arial", 11)).pack(pady=(20, 5))
tk.Entry(root, textvariable=password, show="*", width=30).pack()

strength_label = tk.Label(root, text="Strength", fg="gray")
strength_label.pack(pady=(2, 10))

btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Encrypt", width=15, command=encrypt_file).pack(side="left", padx=10)
tk.Button(btn_frame, text="Decrypt", width=15, command=decrypt_file).pack(side="right", padx=10)

root.mainloop()
