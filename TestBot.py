from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

driver = webdriver.Chrome()

url = 'https://www.instagram.com/'
driver.get(url)

username = 'teobear322'
password = 'Chess101'

#username
#xpath - /html/body/div[1]/div/div/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input
driver.implicitly_wait(10)
driver.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(username)

#password
driver.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(password)

#login button
driver.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()

driver.implicitly_wait(10)

#Not now button
driver.find_element("xpath", '/html/body/div[1]/section/main/div/div/div/div/button').click()

#Not Now 2 Button
driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()

driver.implicitly_wait(10)

driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()

driver.implicitly_wait(10)

driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()

#type name into messenger
driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input').send_keys("itsday_g")

driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[3]/button/div').click()

#Next Button
driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button/div').click()

driver.implicitly_wait(10)

#Text
driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys('I just texted u off a bot niggggggaaaaaa')

driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
print("Message successful")



