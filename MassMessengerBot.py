from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

driver = webdriver.Chrome()

url = 'https://www.instagram.com/'
driver.get(url)

username = 'teobear322'
password = 'Chess101'

wait_time = 10

person = 'miriam.oke'

text = 'I just texted u off a bot niggggggaaaaaa'

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
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()

def message_page(user):
    #type name into messenger
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
    #Account Clicker
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[3]/button/div').click()
    #Next Button
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button/div').click()
    driver.implicitly_wait(wait_time)

def send_message(text):
    #Text
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(text)

    #Send
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
    print("Message successful")

sign_in('teobear322','Chess101')
page_contents()
message_page(person)
send_message("HAHAHAHAHAHAHAH IT REALLY WORKS. You got texted off of a bot made by the glorius Mateo Brown. This is only the first step in my plan. You have been warned by the Loud House. In one month you will learn the true extent of my power")