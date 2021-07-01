

import time


import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.firefox.options import Options



#get the web-driver
firefox_browser = webdriver.Firefox(executable_path='./geckodriver')

#you have to add your own web-driver
def start_up():
    #login in
    message_box = firefox_browser.get('https://www.facebook.com/')
    time.sleep(1)
    


    time.sleep(2)

    #Mail
    message_box = firefox_browser.find_element_by_xpath('//*[@id="email"]')
    message_box.click()
    message_box.send_keys('Wiztro@web.de')
    message_box = firefox_browser.find_element_by_xpath('//*[@id="pass"]')
    #pwd
    message_box.click()
    message_box.send_keys('AYQCJeY92ZJfvcA')
    message_box = firefox_browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]')
    message_box.click()


def uploadpic(path_img, caption):

    #message_box = firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[3]/span/div')
    #message_box.click()
    #time.sleep(2)
    #message_box = firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div')
    #message_box.click()
    time.sleep(2)
    message_box = firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]')
    message_box.click()
    time.sleep(2)
    pyautogui.write(path_img)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    cap = firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div')
    cap.send_keys(caption)
    time.sleep(2)
    message_box = firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div')
    message_box.click()

    #cap =  WebDriverWait(webdriver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div')))
    #cap.send_key(caption)
    #message_box = WebDriverWait(webdriver, 20).until(EC.presence_of_element_located(
    #    (By.XPATH,
    #     '/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[3]')))
    #message_box.click()













if __name__ == '__main__':
    start_up()
    uploadpic('test1.jpg', 'Hallo')


