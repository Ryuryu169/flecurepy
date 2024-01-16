import requests
import hashlib
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from .settings import service_url, service_local_url

def get_cookie(keypath):
    with open(keypath, "r") as f:
        file = f.read()
    file = json.loads(file)
    cookie = file["cookie"]
    service = file["service"]
    return cookie, service


def get_key(filepath, debug=False):
    print("Getting key")
    cookie, service = get_cookie(filepath)
    url = service_url
    if debug:
        url = service_local_url
    res = requests.get(url + "?cookie=" + cookie + "&service=" + service + "&cli=1")
    print(res.text)
    return hashlib.sha256(res.text.encode()).digest()


def encrypt_file(key, filename):
    data = ""
    with open(filename, "rb") as f:
        data = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    with open(filename, "wb") as f:
        f.write(ciphertext)


def decrypt_file(key, filename):
    data = ""
    with open(filename, "rb") as f:
        data = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(data), AES.block_size)

    with open(filename, "wb") as f:
        f.write(plaintext)


if __name__ == "__main__":
    encrypt_file()
