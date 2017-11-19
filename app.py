import time
import json
import random
from flask import Flask, request, json
app = Flask(__name__)

# Wind, solar, nuclear, fossil
input_to_ghg_map = {
            "Nuclear_Investment": -0.5,
            "Solar_Investment": -0.3,
            "Wind_Investment": -0.2,
            "Fossil_Investment": 1.5}

jsonObject = {
        'Money': 100,
        'Emissions Per Year (GHG)': 200,
        'GHG': 1000000,
        'Start_Year': 2017,
        'Curr_Year': 2017,
        'Solar_Investment': 0,
        'Wind_Investment': 0,
        'Nuclear_Investment': 0,
        'Fossil_Investment': 0,
        'GDP': 1000,
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

def update_climate(jsonObject):
    jsonObject['Curr_Year'] += 1
    jsonObject['GDP'] *= 1.01
    jsonObject['Money'] += jsonObject['GDP'] * .01
    pass

def hurCalc(carbon):
    x = random.random()
    carbon += x/2
    return carbon > 1
    # if true, hurricane occurs

def ACCalc(carbon, fSpent, nSpent):
    x = random.random()
    twoSpent = fSpent + nSpent
    carbon += twoSpent/degree + x
    return carbon > 1
    # if true, armed conflict occurs

def agriCalc(carbon, fSpent):
    x = random.random()
    carbon += fSpent/degree + x
    return carbon
    # adds to economy growth

def ecoCalc(carbon, sSpent, wSpent, nSpent, fSpent):
    x = random.random()
    totalSpent = sSpent + wSpent + nSpent + fSpent
    carbon += totalSpent/degree + x
    return carbon
    # defines economic growth

def update_ghg(jsonObject, input_to_ghg_map):
   total_budget = jsonObject['Solar_Investment'] \
                  + jsonObject['Wind_Investment'] \
                  + jsonObject['Nuclear_Investment'] \
                  + jsonObject['Fossil_Investment']
   ghg_max_pos_val = total_budget * input_to_ghg_map['Fossil_Investment']
   ghg_max_neg_val = total_budget * input_to_ghg_map['Solar_Investment'] * -1.0
   ghg_temp_val = jsonObject['Solar_Investment']* input_to_ghg_map['Solar_Investment'] \
                  + jsonObject['Wind_Investment']* input_to_ghg_map['Wind_Investment'] \
                  + jsonObject['Nuclear_Investment']* input_to_ghg_map['Nuclear_Investment'] \
                  + jsonObject['Fossil_Investment']* input_to_ghg_map['Fossil_Investment']
   if ghg_temp_val >= 0:
       ghg_fraction = 1.0 * ghg_temp_val / ghg_max_pos_val
   else:
       ghg_fraction = 1.0 * ghg_temp_val / ghg_max_neg_val
   return (ghg_temp_val,ghg_fraction)

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
        jsonObject['Wind_Investment'] += 1
        jsonObject = update_climate()
        return json.dumps(jsonObject)

@app.route('/nuclear/', methods=['POST'])
def nuclear():
    if request.method == 'POST':
        global jsonObject
        jsonObject = request.get_json()
        jsonObject['Nuclear_Investment'] += 1
        jsonObject = update_climate()
        return json.dumps(jsonObject)

@app.route('/solar/', methods=['POST'])
def solar():
    if request.method == 'POST':
        global jsonObject
        jsonObject = request.get_json()
        jsonObject['Solar_Investment'] += 1
        jsonObject = update_climate()
        return json.dumps(jsonObject)

@app.route('/fossil/', methods=['POST'])
def fossil():
    if request.method == 'POST':
        global jsonObject
        jsonObject = request.get_json()
        jsonObject['Fossil_Investment'] += 1
        jsonObject = update_climate()
        return json.dumps(jsonObject)

if __name__ == "__main__":
    app.run(debug=True)
