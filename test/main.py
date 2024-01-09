from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from bs4 import BeautifulSoup
import requests
import time


driver = webdriver.Safari()
driver.get("http://localhost:4000/")

cookie = ""
gitId = ""

while True:
    try:
        driver.current_url
        text = driver.page_source
        time.sleep(1)
    except NoSuchWindowException:
        soup = BeautifulSoup(text, "html.parser")
        hidden_message = soup.find("p", {"hidden": ""}).text
        cookie, gitId = hidden_message.split(" ")
        print("cookie : " + cookie)
        break

response = requests.get(f"http://localhost:4000/create_service?cookie={cookie}&service=hello&" + "role={Ryuryu169}")
print("The key is : " + response.text)

key_response = requests.get(f"http://localhost:4000/get_key?cookie={cookie}&service=hello")
print("The key is : " + key_response.text)
