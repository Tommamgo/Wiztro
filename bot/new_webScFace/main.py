import time

import os
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

    #Profil
    message_box = firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/a')
    message_box.click()
    time.sleep(1)

    message_box = firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/a')
    message_box.click()
    time.sleep(1)

    ele = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div/div[1]')))
    ele.send_keys("./test.jpg")

    #








#function will be send a single Message to somebody
def messager(name, text):
    #get the Pive Button re




    #message_box.send_keys(name)
    #choose Name
    usr = firefox_browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
    usr.click()
    #insert text
    message_box = firefox_browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
    message_box.send_keys(text)
    #send
    message_box = firefox_browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[3]/button')
    message_box.click()
    #get pic
    time.sleep(1)
    message_box = firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div/div[1]')
    message_box.click()










if __name__ == '__main__':
    start_up()


