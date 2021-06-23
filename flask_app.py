# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, send_file, request
from time import strftime, gmtime
import git
from flask import Response
#import für das Bot File
#from bot.bot_main import inst_pic_post


app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
#app.config.from_object(__name__)

def get_the_time():
    dt_gmt = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    return dt_gmt

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('wiztro.pythonanywhere.com')
        origin = repo.remotes.originorigin.pull()

        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@app.route('/landing')
def landing():
    return render_template('LANDING_PAGE.html')

@app.route('/start')
def start():
    return render_template('start.html')
@app.route('/generator_1.html')
def generator_1():
    return render_template('generator_1.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/static/img/Logo.png", methods=['GET'])
def img_logo():
    return send_file("static/img/Logo.png", mimetype='image/gif')

@app.route("/static/img/Wiztro_Logo.png", methods=['GET'])
def img2():
    if request.method == 'GET':
        return send_file("static/img/Wiztro_Logo.png", mimetype='image/gif')

@app.route("/static/img/Profile_Logo.png", methods=['GET'])
def img3():
    if request.method == 'GET':
        return send_file("static/img/Profile_Logo.png", mimetype='image/gif')

@app.route("/static/img/stempelkarte_oko.png", methods=['GET'])
def img4():
    if request.method == 'GET':
        return send_file("static/img/stempelkarte_oko.png", mimetype='image/gif')





#Das ist für dich zu Hause, auskommentieren und los geht es
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=1337, debug=True)
