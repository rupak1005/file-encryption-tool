#  File Encryptor GUI

A simple, secure, and cross-platform file encryption and decryption tool built with Python and Tkinter.

>  Encrypt any file using a password-based encryption algorithm.  
>  Minimal GUI without external UI dependencies.  
>  Password strength checker built-in.  

---



##  Live Link : https://file-encryption-tool.streamlit.app/


##  Preview

![image](https://github.com/user-attachments/assets/31768327-a925-454c-b761-56d859979108)


![image](https://github.com/user-attachments/assets/7faaee24-b850-487f-8c4e-6abeb6a2368e)


---

##  Features

-  **AES-level encryption** using [cryptography](https://cryptography.io/en/latest/) and Fernet (symmetric encryption)
-  **Password-based key derivation (PBKDF2 + SHA256 + Salt)**
-  **Real-time password strength meter**
-  File selection with built-in file dialog
-  Cross-platform GUI with native `tkinter` (no `customtkinter`, no `tkinterDnD`)
-  Encrypt or decrypt any type of file
-  Simple error messages and friendly alerts

---

##  How it Works

1. You select a file and enter a password.
2. The password is **securely converted into an encryption key** using:
   - PBKDF2HMAC
   - SHA256
   - Salt (random 16 bytes per file)
3. The tool uses the [Fernet encryption scheme](https://cryptography.io/en/latest/fernet/) to encrypt/decrypt the file.
4. Encrypted file is saved as: `filename.ext.secure`
5. Decrypted file is saved as: `filename_decrypted`

---

##  Tech Stack

- **Python 3.8+**
- `tkinter` (built-in)
- `cryptography` (`pip install cryptography`)

---

##  Getting Started

###  Requirements

- Python 3.8+
- `cryptography` module

```bash
pip install cryptography
```

---

##  Running the App

```bash
python file_encryptor_gui.py
```

---

##  Packaging Options

###  Linux `.AppImage`

1. Build standalone executable:
   ```bash
   pip install pyinstaller
   pyinstaller --noconsole --onefile file_encryptor_gui.py
   ```

2. Structure for AppImage:
   ```
   FileEncryptor/
   ├── AppRun
   ├── file_encryptor_gui.desktop
   ├── icon.png
   └── usr/
       └── bin/
           └── file_encryptor_gui
   ```

3. Package with [AppImageTool](https://github.com/AppImage/AppImageKit):
   ```bash
   ./appimagetool-x86_64.AppImage FileEncryptor
   ```

---

###  Windows `.exe`

On Windows:

```bash
pyinstaller --noconsole --onefile file_encryptor_gui.py
```

On Linux (cross-compiling, optional):

```bash
sudo apt install wine
pyinstaller --onefile --noconsole --windowed file_encryptor_gui.py
```

---

##  Security Note

- This tool uses:
  - AES-128 encryption via `Fernet`
  - 390,000 iterations of PBKDF2 with a 16-byte random salt
- Your password is **never stored or transmitted**
- Salt is prepended to the output file (required for decryption)
- Best used with strong, unique passwords

---

## Project Structure

```text
.
├── file_encryptor_gui.py
├── README.md
├── LICENSE
├── icon.png (optional)
├── dist/
│   └── file_encryptor_gui
└── build/
```

---

##  Author

**Rupak**  
 GitHub: [@rupak1005](https://github.com/rupak1005)

---

##  License

This project is licensed under the [MIT License](LICENSE).

---

