import urllib.request
import time
#Try chatch bolck ob es geht wenn nicht dann kann man es lasen
#dann löschen und dem Server bescheid geben
#urllib.request.urlretrieve("https://wiztro.pythonanywhere.com/static/img/stempelkarte_oko.png", "local-filename.png")

try:
    urllib.request.urlretrieve("https://wiztro.pythonanywhere.com/static/img/bild_1.png", "nice.png")
    #hier kommt die post funktion
except:
    print('hallo')
    time.sleep(60)
