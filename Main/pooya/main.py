from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from cookie import collect_cookie, start_with_cookies
import os

name = os.getenv('USER')

chrome_driver_path = f'/home/{name}/Desktop/Personal-Project/Main/pooya/chromedriver'
service = Service(chrome_driver_path)
print(name)
collect_cookie(name)
