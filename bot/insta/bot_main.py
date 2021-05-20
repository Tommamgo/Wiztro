from instabot import Bot
import os
import time
import shutil, sys
#https://developers.facebook.com/docs/graph-api/reference/user/picture/
"""
    für die Facebook Api wird eine Key Token benoetigt
    dieser wird irgenwie ueber den Accout generiert
    
    Der Code sollte dann aber gehen:
    
    graph = facebook.GraphAPI(oauth_access_token)
    photo = open("picture.jpg", "rb")
    graph.put_object("me", "photos", message="You can put a caption here", source=photo.read())
    photo.close()
"""


def inst_pic_post(user, pwd):
    bot = Bot()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    bot.login(username=user,
              password=pwd)
    source = "img/test.jpg"
    destination = "img/hallo.jpg"
    shutil.copyfile(source, destination)
    bot.upload_photo("img/hallo.jpg", caption="Business-OS")


if __name__ == "__main__":
    inst_pic_post("wiztro","RD5SyLm7kQePT4R" )
    # Probleme mit der Lib deswegen immer den Folder wieder löschen
    os.remove("config")
