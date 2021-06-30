from instabot import Bot


bot = Bot()

bot.login(username = "wiztroos422",
		password = "wert66LLa")

# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo
bot.upload_photo("./01.jpg",
				caption ="Technical Scripter Event 2019")

