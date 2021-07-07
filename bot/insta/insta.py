# coding=utf-8
from instabot import Bot
import time
import os

if __name__ == "__main__":
    bot = Bot()
    bot.login(username='wiztro',password='RD5SyLm7kQePT4R')
    while True:
        if(os.path.isfile('./hallo1.jpeg')):
            bot.upload_photo("./hallo1.jpeg", caption="Hallo")
            time.sleep(1)
            #os.remove('./hallo1.jpeg')
            os.remove('./hallo1.jpeg.REMOVE_ME')
        

