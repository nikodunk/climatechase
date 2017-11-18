import time
import json
from flask import Flask, request, json
app = Flask(__name__)

# Wind, solar, nuclear, fossil
reduction_rates = {
            "nuclear": .5,
            "solar": .3,
            "wind": .2,
            "fossil": 1.5}

jsonObject = {
        'Money': 1000000000000,
        'Emissions Per Year (GHG)': 200,
        'GHG': 1000000,
        'Start_Year': 2017,
        'Curr_Year': 2017,
        'Solar_Investment': 0,
        'Wind_Investment': 0,
        'Nuclear_Investment': 0,
        'Fossil_Investment': 0,
        'GDP': 18566900000000,
        'Sea_Levels': 0,
        'Electricity_Price': 0,
        'Agriculture': 0,

        'Risk_of_Hurricane': 0,
        'Hurricanes_Happen': False,
        'Number_of_Hurricanes': 0,

        'Risk_of_Riots': 0,
        'Riots_Happen': False,
        'Number_of_Riots': 0,

        'Risk_of_Famines': 0,
        'Famines_Happen': False,
        'Number_of_Famines': 0,

        'Risk_of_Recessions': 0,
        'Recessions_Happen': False,
        'Number_of_Recessions': 0,

        'GHG': 0,
        'Game_Over': False
    }

#########################################################
# Processing & Trigger Functions
#########################################################

def change_wind(jsonObject):
    pass
    # 1) add money to wind investment
    # 2) Calculate probability of certain action due to wind investment (above/below threshold)
    #     a) Probability of something good happening increases the more wind investment we have
    #     b) Probability of something bad happening increases the longer the game runs (unless we invested properly)
    # 3) Return that something happens

def update_climate():
    pass

#########################################################
# Routes
#########################################################

@app.route("/")
def home():
    jsonObject['Curr_Year'] += 1
    return json.dumps(jsonObject)

@app.route('/instructions/')
def instructions():
    return json.dumps(jsonObject)

@app.route('/about/')
def about():
    return json.dumps(jsonObject)

@app.route('/play/')
def play():
    return json.dumps(jsonObject)

@app.route('/give_data/', methods=['GET'])
def give_data():
    if request.method == 'GET':
        return str([jsonObject])


@app.route('/receive_data/', methods=['POST'])
def receive_data():
    global jsonObject
    if request.method == 'POST':
        jsonObject = request.get_json()
        return "Successfully gotten Front-End code."

@app.route('/lose/', methods=['GET'])
def lose():
    global jsonObject
    jsonObject['Money'] -= 1000000000000
    jsonObject['Game_Over'] = True
    return json.dumps(jsonObject)

@app.route('/win/', methods=['GET'])
def win():
    global jsonObject
    jsonObject['Money'] += 1
    jsonObject['Game_Over'] = False
    return json.dumps(jsonObject)


#########################################################
# Button Routes
#########################################################

@app.route('/wind/', methods=['POST'])
def wind():
    if request.method == 'POST':
        global jsonObject
        jsonObject = request.get_json()
        jsonObject['Money'] -= 1000000
        jsonObject['Wind_Investment'] += 1000000
        update_climate()
        return json.dumps(jsonObject)

@app.route('/nuclear/', methods=['POST'])
def nuclear():
    if request.method == 'POST':
        global jsonObject
        jsonObject = request.get_json()
        jsonObject['Money'] -= 1000000
        jsonObject['Nuclear_Investment'] += 1000000
        update_climate()
        return json.dumps(jsonObject)

@app.route('/solar/', methods=['POST'])
def solar():
    if request.method == 'POST':
        global jsonObject
        jsonObject = request.get_json()
        jsonObject['Money'] -= 1000000
        jsonObject['Solar_Investment'] += 1000000
        update_climate()
        return json.dumps(jsonObject)

@app.route('/fossil/', methods=['POST'])
def fossil():
    if request.method == 'POST':
        global jsonObject
        jsonObject = request.get_json()
        jsonObject['Money'] -= 1000000
        jsonObject['Fossil_Investment'] += 1000000
        update_climate()
        return json.dumps(jsonObject)

if __name__ == "__main__":
    app.run(debug=True)
