# coding=utf-8
#from instabot import Bot
import requests
import urllib.parse as urlparse
from urllib.parse import urlencode
from PIL import Image
import os
import time
import shutil, sys
#https://developers.facebook.com/docs/graph-api/reference/user/picture/
import urllib.request
import time
#Try chatch bolck ob es geht wenn nicht dann kann man es lasen
#dann loeschen und dem Server bescheid geben
#urllib.request.urlretrieve("https://wiztro.pythonanywhere.com/static/img/stempelkarte_oko.png", "local-filename.png")
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


"""
    für die Facebook Api wird eine Key Token benoetigt
    dieser wird irgenwie ueber den Accout generiert
    
    Der Code sollte dann aber gehen:
    
    graph = facebook.GraphAPI(oauth_access_token)
    photo = open("picture.jpg", "rb")
    graph.put_object("me", "photos", message="You can put a caption here", source=photo.read())
    photo.close()
"""
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
    time.sleep(1)
    message_box = firefox_browser.find_element_by_xpath('//*[@id="pass"]')
    #pwd
    message_box.click()
    message_box.send_keys('AYQCJeY92ZJfvcA')
    message_box = firefox_browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]')
    message_box.click()

def uploadpic(path_img, caption):
    print("1")
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
    print("7")

    #cap =  WebDriverWait(webdriver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div')))
    #cap.send_key(caption)
    #message_box = WebDriverWait(webdriver, 20).until(EC.presence_of_element_located(
    #    (By.XPATH,
    #     '/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[3]')))
    #message_box.click()





def inst_pic_post(user, pwd):
    bot = Bot()
    #t = time.localtime()
    #current_time = time.strftime("%H:%M:%S", t)
    bot.login(username=user,
              password=pwd)
    #source = "img/test.jpg"
    #destination = "img/hallo.jpg"
    #shutil.copyfile(source, destination)

    bot.upload_photo("./hallo.jpeg", caption="Business-OS")

def isnew():
    temp = serv_del()
    print(temp)
    
    try:
        if (temp != 0): 
            print(temp)
            urllib.request.urlretrieve("https://wiztro.pythonanywhere.com/" + str(temp), "hallo.png")
            #um wandel von dem Bild
            print("hall")
            time.sleep(2)
            im = Image.open('./hallo.png')
            rgb_im = im.convert('RGB')
            rgb_im.save('hallo.jpeg')
            time.sleep(1)
            #inst_pic_post('wiztro', 'RD5SyLm7kQePT4R')
            #loeschen den files
            time.sleep(1)
            uploadpic('hallo.jpeg', 'Hallo')
            os.remove('./hallo.png')
            os.remove('./hallo.jpeg')
            print("Sachen")
            print("nice")
            #hier kommt die post funktion
    except:
        print('hallo')
        time.sleep(1)
    


def serv_del():
    url = 'https://wiztro.pythonanywhere.com/get?name=1'
    temp = requests.get(url).text
    return temp
    """
    if(temp != '0'):
        return cutme(temp)
    else:
        return temp
    #return urlparse.urlparse(url)
    """
def cutme(text):
    return text[3:]



if __name__ == "__main__":
    #inst_pic_post("wiztro","RD5SyLm7kQePT4R" )
    start_up()
    while(True):
        isnew()
    # Probleme mit der Lib deswegen immer den Folder wieder lowschen
    #os.remove("config")
