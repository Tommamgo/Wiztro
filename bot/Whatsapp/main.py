from selenium import webdriver
import time

#get the web-driver
firefox_browser = webdriver.Firefox(executable_path='./geckodriver')

#you have to add your own web-driver
def start_up():
    #login in
    firefox_browser.get('https://web.whatsapp.com/')
    #linke the qrcode
    #sorry keine Zeit das zu fixxen dauert ewig da die das nach jedem Aufruf ändern
    time.sleep(10)




#function will be send a single Message to somebody
def messager(name, text):
    #search Name
    message_box = firefox_browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
    message_box.send_keys(name)
    #choose Name
    usr = firefox_browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
    usr.click()
    #insert text
    message_box = firefox_browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
    message_box.send_keys(text)
    #send
    message_box = firefox_browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[3]/button')
    message_box.click()



if __name__ == "__main__":
    start_up()

    #messager('Business OS', 'Ich bins nochmal, wie zur Hölle Lade ich in Whatsapp Web ein Bild in meinen Status?')
    messager('Vanessa ♥️ Lenz', 'Hallo, ich bin der Server und wollte mich mal melden. --Whatsapp Server geht')
    #for i in range(100):
    #    messager('Lukas B', 'hoffentlich nerve ich dich!! ')

