from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def collectcookie():
    chrome_driver_path = '/home/erfan-hooman/Desktop/Personal-Project/Main/pooya/chromedriver'
    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=service)
    driver.get("https://pooya.kashanu.ac.ir/gateway/PuyaAuthenticate.php")

    gov_button = driver.find_element(By.CLASS_NAME, "ssologin")
    gov_button.click()

    number = "09037665074"
    captcha = input("Enter the captcha: ")

    number_input = driver.find_element(By.ID, "username")
    number_input.send_keys(number)

    captcha_input = driver.find_element(by='css selector', value='.captcha_section > :nth-child(2) > .form-control')
    captcha_input.send_keys(captcha)

    send_button = driver.find_element(By.ID, "send-otp-form-btn")
    send_button.click()

    number1 = driver.find_element(By.CLASS_NAME, "first number")
    number2 = driver.find_element(By.CLASS_NAME, "second number")
    number3 = driver.find_element(By.CLASS_NAME, "third number")
    number4 = driver.find_element(By.CLASS_NAME, "fourth number")
    number5 = driver.find_element(By.CLASS_NAME, "fifth number")

    number1.send_keys(input("enter 1 number"))
    number2.send_keys(input("enter 2 number"))
    number3.send_keys(input("enter 3 number"))
    number4.send_keys(input("enter 4 number"))
    number5.send_keys(input("enter 5 number"))

    l_button = driver.find_element(By.ID, "submitLogin")
    l_button.click()

    cookies = driver.get_cookies()

    with open('cookies.json', 'w') as f:
        json.dump(cookies, f)

    driver.quit()