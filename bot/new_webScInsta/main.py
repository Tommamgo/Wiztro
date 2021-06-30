import time

import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

browser = webdriver.Chrome('./chromedriver')

def start_insta():
    message = browser.get('https://www.instagram.com/accounts/login/')
    time.sleep(5)

    message = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    message.click()
    message.send_keys('wiztro')

    message = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    message.click()
    message.send_keys('RD5SyLm7kQePT4R')

    message = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
    message.click()

def start_facebook():
    message = browser.get('https://www.facebook.com/')
    time.sleep(5)

    message = browser.find_element_by_xpath('//*[@id="email"]')
    message.click()
    message.send_keys('Wiztro@web.de')

    message = browser.find_element_by_xpath('//*[@id="pass"]')
    message.click()
    message.send_keys('AYQCJeY92ZJfvcA')

    message = browser.find_element_by_xpath('//*[@id="u_0_j_Di"]')
    message.click()


if __name__ == '__main__':
    #start_insta()
    start_facebook()