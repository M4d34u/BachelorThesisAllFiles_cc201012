
from flask import Flask
from flask import request
import atexit
from time import sleep
import peltier

app = Flask(__name__)

@app.route("/")
def root():
    return "Incinerator API"

@app.route('/mode', methods = ['GET'])
def get_mode():
    return {'mode': mode}

@app.route('/mode', methods = ['PUT'])
def set_mode():
    global mode
    mode = request.get_json()['mode']
    peltier.set_mode(mode)
    return {'mode': mode}

atexit.register(peltier.gpiocleanup)
peltier.init()
