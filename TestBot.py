from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


driver = webdriver.Chrome()

url = 'https://www.instagram.com/'
driver.get(url)
