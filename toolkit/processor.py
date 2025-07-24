import base64
import hashlib
from cryptography.fernet import Fernet
import os

def get_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def FileCipher(inputfile, outputfile, password, work="E"):
    key = get_key(password)
    fernet = Fernet(key)

    with open(inputfile, 'rb') as f:
        data = f.read()

    if work == "E":
        # Encrypt
        result = fernet.encrypt(data)
        print(f"[Success] File encrypted and saved to {outputfile}")
    elif work == "D":
        # Decrypt
        try:
            result = fernet.decrypt(data)
            print(f"[Success] File decrypted and saved to {outputfile}")
        except Exception as e:
            print("[Error] Failed to decrypt. Wrong password?")
            return
    else:
        print("[Error] Invalid mode. Use 'E' for encrypt or 'D' for decrypt.")
        return

    with open(outputfile, 'wb') as f:
        f.write(result)
