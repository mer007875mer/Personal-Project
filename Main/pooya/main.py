from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from cookie import collectcookie

chrome_driver_path = '/home/erfan-hooman/Desktop/Personal-Project/Main/pooya/chromedriver'
service = Service(chrome_driver_path)


collectcookie()

# driver = webdriver.Chrome(service=service)
# driver.get("https://pooya.kashanu.ac.ir/gateway/PuyaAuthenticate.php")
#
# username = "40121160031"
# password = "Mer@@7875"
#
# username_input = driver.find_element(By.ID, 'UserID')
# password_input = driver.find_element(By.ID, 'DummyVar')
# captcha_input = driver.find_element(By.ID, 'capt')
#
# username_input.send_keys(username)
# password_input.send_keys(password)
# captcha = input("Please enter the captcha value: ")
# captcha_input.send_keys(captcha)
#
# login_button = driver.find_element(By.CLASS_NAME, 'login100-form-btn')
# login_button.click()