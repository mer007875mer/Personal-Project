from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from PIL import Image
import io
import pytesseract


chrome_driver_path = '/home/erfan-hooman/Desktop/Main/pooya-kashan/chromedriver'
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get("https://pooya.kashanu.ac.ir/gateway/PuyaAuthenticate.php")

enter = driver.find_element(By.CLASS_NAME, '')

driver.quit()
