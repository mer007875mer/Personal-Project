from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import time


def collect_cookie(name):
    chrome_driver_path = f'/home/{name}/Desktop/Personal-Project/Main/pooya/chromedriver'
    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=service)
    driver.get("https://pooya.kashanu.ac.ir/gateway/PuyaAuthenticate.php")

    gov_button = driver.find_element(By.CLASS_NAME, "ssologin")
    gov_button.click()

    try:
        start_with_cookies(name)
    except Exception as e:
        print(e)
        number = "09037665074"
        captcha = input("Enter the captcha: ")

        number_input = driver.find_element(By.ID, "username")
        number_input.send_keys(number)

        captcha_input = driver.find_element(by='css selector', value='.captcha_section > :nth-child(2) > .form-control')
        captcha_input.send_keys(captcha)

        send_button = driver.find_element(By.ID, "send-otp-form-btn")
        send_button.click()

        number1 = driver.find_element(By.CSS_SELECTOR, ".first")
        number2 = driver.find_element(By.CSS_SELECTOR, ".second")
        number3 = driver.find_element(By.CSS_SELECTOR, ".third")
        number4 = driver.find_element(By.CSS_SELECTOR, ".fourth")
        number5 = driver.find_element(By.CSS_SELECTOR, ".fifth")

        number1.send_keys(input("enter 1 number: "))
        number2.send_keys(input("enter 2 number: "))
        number3.send_keys(input("enter 3 number: "))
        number4.send_keys(input("enter 4 number: "))
        number5.send_keys(input("enter 5 number: "))

        l_button = driver.find_element(By.ID, "submitLogin")
        l_button.click()

        time.sleep(30)

        open_button = driver.find_element(By.CSS_SELECTOR, "body > div > form > button")
        open_button.click()

        cookies = driver.get_cookies()

        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)

        time.sleep(30)

        driver.quit()


def start_with_cookies(name):
    chrome_driver_path = f'/home/{name}/Desktop/Personal-Project/Main/pooya/chromedriver'
    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=service)

    with open('cookies.json', 'r') as f:
        cookies = json.load(f)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get("https://pooya.kashanu.ac.ir/gateway/PuyaAuthenticate.php")

    time.sleep(15)

    open_button = driver.find_element(By.CSS_SELECTOR, "body > div > form > button")
    open_button.click()

    time.sleep(15)