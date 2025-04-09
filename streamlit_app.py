# streamlit_app.py
import streamlit as st
from encryption import encrypt_file, decrypt_file  # your existing functions

st.title("🔐 File Encryption Tool")

mode = st.radio("Select mode", ["Encrypt", "Decrypt"])
uploaded_file = st.file_uploader("Upload file", type=None)
password = st.text_input("Enter password", type="password")

if st.button("Go") and uploaded_file and password:
    input_path = f"./temp_input_{uploaded_file.name}"
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    output_path = f"./processed_{uploaded_file.name}"
    try:
        if mode == "Encrypt":
            encrypt_file(input_path, output_path, password)
        else:
            decrypt_file(input_path, output_path, password)

        with open(output_path, "rb") as f:
            st.download_button("Download", f, file_name=output_path)

    except ValueError as e:
        st.error(str(e))
