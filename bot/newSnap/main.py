from snapchat import Snapchat

def run():

    s = Snapchat()
    s.login('wiztroesse21', 'ksdnrgoipq')

    # Send a snapchat
    media_id = s.upload(Snapchat.MEDIA_IMAGE, 'filename.jpg')
    s.send(media_id, 'recipient')

    # Get all snaps
    snaps = s.get_snaps()

    # Download a snap
    s.get_media(snap['id'])

    # Clear snapchat history
    s.clear_feed()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
