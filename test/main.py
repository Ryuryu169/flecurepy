from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Go to the URL
driver.get("http://localhost:4000/")

# Get the page source (HTML)
html = driver.page_source

# # Print the result
# print(html)

# Close the tab or window
# tmpUrl = (
#     "http://localhost:4000/create_service" + "?service=helloworld" + "&role=[Ryuryu169]"
# )
# tmpRes = requests.get(tmpUrl)
# nextUrl = (
#     "http://localhost:4000/get_key" + "?service=helloworld" + "&cookie=" + str(cookie)
# )
# nextRes = requests.get(nextUrl)
# key = nextRes
# print(key)


# fernet = Fernet(key)
# with open("test.txt", "rb") as file:
#     original = file.read()

# encrypted = fernet.encrypt(original)

# with open("test.txt", "wb") as encrypted_file:
#     encrypted_file.write(encrypted)


# This should do

# with open("test.txt", "rb") as encrypted_file:
#     encrypted_data = encrypted_file.read

# recover = fernet.decrypt(encrypted_data)

# with open("test.txt", "rb") as decrypted_file:
#     decrypted_file.write(recover)
