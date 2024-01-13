import subprocess

# Install the package
subprocess.run(["pip", "install", "."], check=True)

# Run the Python script
import flecurepy

keypath = ".flecure/settings.json"
filepath = "result/example.txt"

key = flecurepy.get_key(keypath)
flecurepy.encrypt_file(key, filepath)
flecurepy.decrypt_file(key, filepath)