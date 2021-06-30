from instabot import Bot
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
#dann löschen und dem Server bescheid geben
#urllib.request.urlretrieve("https://wiztro.pythonanywhere.com/static/img/stempelkarte_oko.png", "local-filename.png")


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
    #t = time.localtime()
    #current_time = time.strftime("%H:%M:%S", t)
    bot.login(username=user,
              password=pwd)
    #source = "img/test.jpg"
    #destination = "img/hallo.jpg"
    #shutil.copyfile(source, destination)

    bot.upload_photo("img/hallo.jpeg", caption="Business-OS")

def isnew():
    try:
        urllib.request.urlretrieve("https://wiztro.pythonanywhere.com/static/img/bild_1.png", "hallo.png")
        #um wandel von dem Bild
        time.sleep(2)
        im = Image.open('./hallo.png')
        rgb_im = im.convert('RGB')
        rgb_im.save('hallo.jpeg')
        time.sleep(1)
        #inst_pic_post('wiztro', 'RD5SyLm7kQePT4R')
        #löschen den files
        os.remove('./hallo.png')
        os.remove('./hallo.jpeg')

    #hier kommt die post funktion
    except:
        print('hallo')
        time.sleep(60)



def serv_del():
    params = {'name': '1'}
    request.get('https://wiztro.pythonanywhere.com/del', params=params)
if __name__ == "__main__":
    #inst_pic_post("wiztro","RD5SyLm7kQePT4R" )
    while(True):
        isnew()
    # Probleme mit der Lib deswegen immer den Folder wieder löschen
    #os.remove("config")
