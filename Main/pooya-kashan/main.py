from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
import io
import pytesseract

def find_captcha(url):
    captcha = driver.find_element(By.ID, "captImg")

    location = captcha.location
    size = captcha.size

    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(io.BytesIO(screenshot))

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    captcha_image = screenshot.crop((left, top, right, bottom))
    captcha_image = captcha_image.convert('L')
    captcha_image = captcha_image.point(lambda x: 0 if x < 128 else 255, '1')

    render = easyocr.Reader(['en'])
    captcha_code = render.readtext(captcha_image)
    print(captcha_code)

    print(f"code : {captcha_code.strip()}")
    return captcha_code


chrome_driver_path = '/home/erfan-hooman/Desktop/Main/pooya-kashan/chromedriver'
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get("https://pooya.kashanu.ac.ir/gateway/PuyaAuthenticate.php")

username = "40121160031"
password = "Mer@@7875"
captcha = find_captcha(url="https://pooya.kashanu.ac.ir/gateway/PuyaAuthenticate.php")

username_input = driver.find_element(By.ID, 'UserID')
password_input = driver.find_element(By.ID, 'DummyVar')
captcha_input = driver.find_element(By.ID, 'capt')

username_input.send_keys(username)
password_input.send_keys(password)
captcha_input.send_keys(captcha)

login_button = driver.find_element(By.CLASS_NAME, 'login100-form-btn')
