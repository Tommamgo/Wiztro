from instabot import Bot
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

    bot.login(username=user,
              password=pwd)

    #keine Ahung ob der path erkannt wird
    bot.upload_photo("img/Logo.png",
                     caption="Business-OS")
