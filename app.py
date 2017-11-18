import time
import json
from flask import Flask
app = Flask(__name__)

jsonObject = [{
        "GDP": "1000000",
        "Emissions": "200GHP"
    }
]

time.start()

@app.route("/")
def hello():
    return str(jsonObject)

@app.route("/hello")
def index():
    return 'Hello, World'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/getData', methods=['GET'])
def getData():
    return 'Hello, World'

if __name__ == "__main__":
    app.run()
