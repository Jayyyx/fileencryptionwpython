import base64
import hashlib
from cryptography.fernet import Fernet
import os

def get_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def FileCipher(inputfile, outputpath, password, work="E"):
    key = get_key(password)
    fernet = Fernet(key)

    with open(inputfile, 'rb') as f:
        data = f.read()

    filename = os.path.basename(inputfile)

    if work == "E":
        result = fernet.encrypt(data)
        print(f"[Success] File encrypted and saved to {outputpath}")
    elif work == "D":
        try:
            result = fernet.decrypt(data)
            print(f"[Success] File decrypted and saved to {outputpath}")
        except Exception:
            print("[Error] Failed to decrypt. Wrong password?")
            return
    else:
        print("[Error] Invalid mode. Use 'E' for encrypt or 'D' for decrypt.")
        return

    # Write the result to the specified output file path directly
    output_dir = os.path.dirname(outputpath)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(outputpath, 'wb') as f:
        f.write(result)
