# 
import requests

url = "http://localhost:3000"

def get_key():
    res = requests.get(url)
    key = res.json()["data"]
    with open("key.txt", "w") as f:
        f.write(key)
    print("key.txt was created.")

if __name__ == "__main__":
    get_key()
