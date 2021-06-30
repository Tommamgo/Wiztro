# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, send_file, request
from time import strftime, gmtime
import git
from flask import Response
#import für das Bot File
#from bot.bot_main import inst_pic_post


app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
#app.config.from_object(__name__)

global get_pic

def get_the_time():
    dt_gmt = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    return dt_gmt

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/Wiztro/Wiztro')
        origin = repo.remotes.origin
        origin.pull()

        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@app.route('/landing')
def landing():
    return render_template('LANDING_PAGE.html')


@app.route('/next')
def next():
    return render_template('next.html')

@app.route('/next_1')
def next1():
    return render_template('next_1.html')

@app.route('/next_2')
def next2():
    return render_template('next_2.html')

@app.route('/next_3')
def next3():
    return render_template('next_3.html')

@app.route('/next_4')
def next4():
    return render_template('next_4.html')





@app.route('/start')
def start():
    return render_template('start.html')
@app.route('/generator_1.html')
def generator_1():
    return render_template('generator_1.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods= ['POST', 'GET'])
def get():
    name = ''
    if request.method == 'POST':
        name =request.args.get('name')
    else:
        name = request.args.get('name')
    if(name == '1'): 
        name = get_pic
        get_pic = '0'
    else:
        name = "nop"

    return name

@app.route('/botfile', methods=['POST', 'GET'])
def botfile():
    get_pic = request.args.get('name')
    return get_pic


@app.route("/static/img/Logo.png", methods=['GET'])
def img_logo():
    return send_file("static/img/Logo.png", mimetype='image/gif')

@app.route("/static/img/Wiztro_Logo.png", methods=['GET'])
def img2():
    if request.method == 'GET':
        return send_file("static/img/Wiztro_Logo.png", mimetype='image/gif')

@app.route("/static/img/del.png", methods= ['GET'])
def dele():
    if request.method == 'GET':
        return send_file("static/img/del.png", mimetype='image/gif')

@app.route("/static/img/Profile_Logo.png", methods=['GET'])
def img3():
    if request.method == 'GET':
        return send_file("static/img/Profile_Logo.png", mimetype='image/gif')

@app.route("/static/img/stempelkarte_oko.png", methods=['GET'])
def img4():
    if request.method == 'GET':
        return send_file("static/img/stempelkarte_oko.png", mimetype='image/gif')


@app.route("/static/img/bild_1.png", methods=['GET'])
def img5():
    if request.method == 'GET':
        return send_file("static/img/bild_1.png", mimetype='image/gif')

@app.route("/static/img/bild_2.png", methods=['GET'])
def img6():
    if request.method == 'GET':
        return send_file("static/img/bild_2.png", mimetype='image/gif')

@app.route("/static/img/bild_3.png", methods=['GET'])
def img7():
    if request.method == 'GET':
        return send_file("static/img/bild_3.png", mimetype='image/gif')

@app.route("/static/img/bild_4.png", methods=['GET'])
def img8():
    if request.method == 'GET':
        return send_file("static/img/bild_4.png", mimetype='image/gif')

@app.route("/static/img/bild_5.png", methods=['GET'])
def img9():
    if request.method == 'GET':
        return send_file("static/img/bild_5.png", mimetype='image/gif')

@app.route("/static/img/bild_6.png", methods=['GET'])
def img10():
    if request.method == 'GET':
        return send_file("static/img/bild_6.png", mimetype='image/gif')

@app.route("/static/img/bild_7.png", methods=['GET'])
def img11():
    if request.method == 'GET':
        return send_file("static/img/bild_7.png", mimetype='image/gif')

@app.route("/static/img/bild_8.png", methods=['GET'])
def img12():
    if request.method == 'GET':
        return send_file("static/img/bild_8.png", mimetype='image/gif')

@app.route("/static/img/bild_9.png", methods=['GET'])
def img13():
    if request.method == 'GET':
        return send_file("static/img/bild_9.png", mimetype='image/gif')

@app.route("/static/img/bild_10.png", methods=['GET'])
def img14():
    if request.method == 'GET':
        return send_file("static/img/bild_10.png", mimetype='image/gif')

@app.route("/static/img/bild_11.png", methods=['GET'])
def img15():
    if request.method == 'GET':
        return send_file("static/img/bild_11.png", mimetype='image/gif')

@app.route("/static/img/bild_12.png", methods=['GET'])
def img16():
    if request.method == 'GET':
        return send_file("static/img/bild_12.png", mimetype='image/gif')

@app.route("/static/img/bild_13.png", methods=['GET'])
def img17():
    if request.method == 'GET':
        return send_file("static/img/bild_13.png", mimetype='image/gif')

@app.route("/static/img/bild_14.png", methods=['GET'])
def img18():
    if request.method == 'GET':
        return send_file("static/img/bild_14.png", mimetype='image/gif')

@app.route("/static/img/bild_15.png", methods=['GET'])
def img19():
    if request.method == 'GET':
        return send_file("static/img/bild_15.png", mimetype='image/gif')

@app.route("/static/img/bild_16.png", methods=['GET'])
def img20():
    if request.method == 'GET':
        return send_file("static/img/bild_16.png", mimetype='image/gif')

@app.route("/static/img/bild_17.png", methods=['GET'])
def img21():
    if request.method == 'GET':
        return send_file("static/img/bild_17.png", mimetype='image/gif')

@app.route("/static/img/bild_18.png", methods=['GET'])
def img22():
    if request.method == 'GET':
        return send_file("static/img/bild_18.png", mimetype='image/gif')





























#Das ist für dich zu Hause, auskommentieren und los geht es
if __name__ == "__main__":
	app.run()
