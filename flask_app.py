
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, send_file, request
from time import strftime, gmtime
import git
#import für das Bot File
#from bot.bot_main import inst_pic_post


app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

def get_the_time():
    dt_gmt = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    return dt_gmt

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('update_server')
        origin = repo.remotes.originorigin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400






@app.route('/')
def index():
    return render_template('index.html')

@app.route("/static/img/Logo.png", methods=['GET'])
def img_logo():
    return send_file("static/img/Logo.png", mimetype='image/gif')