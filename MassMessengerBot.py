from multiprocessing.connection import wait
from operator import truediv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import random

driver = webdriver.Chrome()

url = 'https://www.instagram.com/'
driver.get(url)

my_username = 'Enter username'
my_password = 'Enter password'

wait_time = 10

targets = ['lor_bernie', 'jordanxalexis2', 'itsday_g', 'elijahrock','miriam.oke']

text = "HAHAHAHAHAHAHAH IT REALLY WORKS. You got texted off of a bot made by the glorius Mateo Brown. This is only the first step in my plan. You have been warned by the Loud House. In one month you will learn the true extent of my power"

time_between_text = 2

def sign_in(username, password):
    driver.implicitly_wait(wait_time)
    #username
    driver.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(username)
    #password
    driver.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(password)
    #login button
    driver.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
    driver.implicitly_wait(wait_time)

def page_contents():
    #Not now button
    driver.find_element("xpath", '/html/body/div[1]/section/main/div/div/div/div/button').click()
    #Not Now 2 Button
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
    driver.implicitly_wait(wait_time)
    #Message Button
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    driver.implicitly_wait(wait_time)
    
def message(user):
    driver.implicitly_wait(wait_time)
    #type name into messenger
    textarea = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
    driver.implicitly_wait(wait_time)
    #Account Clicker
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[3]/button/div').click()
    driver.implicitly_wait(wait_time)
    #Next Button
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button/div').click()

def send_message(text):
    try:
        driver.implicitly_wait(wait_time)
        #Text
        driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(text)
        driver.implicitly_wait(wait_time)
        #Send
        driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
        return True
    
    except Exception as err:
        print(err)
        return False

sign_in(my_username, my_password)
page_contents()
for target in targets:
    #Write Button
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
    message(target)
    if message:
        print(f"Message to \"{target}\" was succesful")
    time.sleep(random.randint(2,3))
    send_message(text)
    time.sleep(time_between_text)
