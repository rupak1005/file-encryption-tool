import os
import base64
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
def encrypt_file(input_path, output_path, password):
    with open(input_path, "rb") as f:
        data = f.read()
    salt = os.urandom(16)
    key = derive_key(password, salt)
    encrypted = Fernet(key).encrypt(data)
    with open(output_path, "wb") as f:
        f.write(salt + encrypted)

# Decrypt file

def decrypt_file(input_path, output_path, password):
    with open(input_path, "rb") as f:
        content = f.read()
    salt = content[:16]
    data = content[16:]
    key = derive_key(password, salt)

    try:
        decrypted = Fernet(key).decrypt(data)
    except InvalidToken:
        raise ValueError("Invalid password or corrupted file.")

    with open(output_path, "wb") as f:
        f.write(decrypted)