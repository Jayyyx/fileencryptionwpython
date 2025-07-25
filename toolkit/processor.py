import base64
import hashlib
from cryptography.fernet import Fernet
import os

def get_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def FileCipher(inputfile, outputdir, password, work="E"):
    key = get_key(password)
    fernet = Fernet(key)

    with open(inputfile, 'rb') as f:
        data = f.read()

    filename = os.path.basename(inputfile)

    if work == "E":
        result = fernet.encrypt(data)
        output_filename = f"encrypted_{filename}.ssb"
        print(f"[Success] File encrypted and saved to {outputdir}")
    elif work == "D":
        try:
            result = fernet.decrypt(data)
            if filename.endswith(".ssb"):
                filename = filename[:-4]  # remove '.ssb'
            output_filename = f"decrypted_{filename}"
            print(f"[Success] File decrypted and saved to {outputdir}")
        except Exception as e:
            print("[Error] Failed to decrypt. Wrong password?")
            return
    else:
        print("[Error] Invalid mode. Use 'E' for encrypt or 'D' for decrypt.")
        return

    full_output_path = os.path.join(outputdir, output_filename)
    with open(full_output_path, 'wb') as f:
        f.write(result)
