import time
import json
import random
from flask import Flask, request, json
app = Flask(__name__)

# Wind, solar, nuclear, fossil
input_to_ghg_map = {
            "nuclear": -0.5,
            "solar": -0.3,
            "wind": -0.2,
            "fossil": 1.5}

print("run")
jsonObject = {
        'Start_Year': 2017,
        'Money': 100,
        'GHG': 1000000,
        'GDP': 1000,
        'Curr_Year': 2017,
        'solar': 0,
        'wind': 0,
        'nuclear': 0,
        'fossil': 0,
        'GDP_Growth': 1.1,
        'economy': 1.1,

        'Sea_Levels': 0,
        'Electricity_Price': 0,
        'Agriculture': 0,

        #'Risk_of_Hurricane': 0,
        'Hurricanes_Happen': False,
        #'Number_of_Hurricanes': 0,

        #'Risk_of_Riots': 0,
        'AC_Happen': False,
        #'Number_of_Riots': 0,

        'GDP_Growth': 0,

        'Game_Over': False
    }

#########################################################
# Processing & Trigger Functions
#########################################################

    # 1) add money to wind investment
    # 2) Calculate probability of certain action due to wind investment (above/below threshold)
    #     a) Probability of something good happening increases the more wind investment we have
    #     b) Probability of something bad happening increases the longer the game runs (unless we invested properly)
    # 3) Return that something happens


def have_lost(jsonObject):
    if jsonObject['Game_Over'] or jsonObject['GDP'] < 0 or jsonObject['Money'] < 0:
        return True
    if jsonObject['Curr_Year'] - jsonObject['Start_Year'] > 200:
        return jsonObject['GHG'] > 1000000

def have_won(jsonObject):
    return jsonObject['GHG'] < 10000

def update_climate(jsonObject):
    if have_won(jsonObject):
        print("You have successfully avoided global warming!")
        return jsonObject
    if have_lost(jsonObject):
        jsonObject['Game_Over'] = True
        print("Global Warming has overtaken the world. Humanity cannot continue.")
        return jsonObject
    jsonObject['Curr_Year'] += 1
    jsonObject['GDP'] = round(jsonObject['GDP'] * jsonObject['GDP_Growth'], 2)
    jsonObject['GDP'] = round(jsonObject['GDP'] * 1.01 + jsonObject['GDP_Growth'], 2)
    jsonObject['GDP'] = round(jsonObject['GDP'] * jsonObject['economy'], 2)
    jsonObject['Money'] = round(jsonObject['Money'] + jsonObject['GDP'] * .01, 2)
    jsonObject['GHG'] = update_ghg(jsonObject, input_to_ghg_map)[1]
    curr_ghg = jsonObject['GHG']
    hurCalc(curr_ghg) = jsonObject['Hurricanes_Happen']
    ACCalc(curr_ghg, jsonObject['fossil'], jsonObject['nuclear']) = jsonObject['AC_Happen']
    agriCalc(curr_ghg, jsonObject['fossil']) = jsonObject['']
    ecoCalc(curr_ghg, jsonObject['solar'], jsonObject['wind'], jsonObject['nuclear'], jsonObject['fossil']) = jsonObject['GDP_Growth']

    return jsonObject

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

def ecoCalc(carbon, sSpent, wSpent, nSpent, fSpent):
    x = random.random()
    totalSpent = sSpent + wSpent + nSpent + fSpent
    carbon += totalSpent / degree + x
    return carbon
    # defines economic growth

def update_ghg(jsonObject, input_to_ghg_map):
   total_budget = jsonObject['solar'] \
                  + jsonObject['wind'] \
                  + jsonObject['nuclear'] \
                  + jsonObject['fossil']
   ghg_max_pos_val = total_budget * input_to_ghg_map['fossil']
   ghg_max_neg_val = total_budget * input_to_ghg_map['solar'] * -1.0
   ghg_temp_val = jsonObject['solar']* input_to_ghg_map['solar'] \
                  + jsonObject['wind']* input_to_ghg_map['wind'] \
                  + jsonObject['nuclear']* input_to_ghg_map['nuclear'] \
                  + jsonObject['fossil']* input_to_ghg_map['fossil']
   if ghg_temp_val >= 0:
       ghg_fraction = 1.0 * ghg_temp_val / ghg_max_pos_val
   else:
       ghg_fraction = 1.0 * ghg_temp_val / ghg_max_neg_val
   return (ghg_temp_val, ghg_fraction)

def lose(jsonObject):
    if jsonObject['Game_Over'] or jsonObject['GDP'] < 0 or jsonObject['Money'] < 0:
        return True
    if jsonObject['Curr_Year'] - jsonObject['Start_Year'] > 200:
        return jsonObject['GHG'] > 1000000

def win(jsonObject):
    return jsonObject['GHG'] < 10000

#########################################################
# Routes
#########################################################

@app.route("/")
def home():
    global jsonObject
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
        jsonObject['wind'] += 1
        jsonObject['Money'] -= input_to_ghg_map['wind']*10
        jsonObject = update_climate(jsonObject)
        return json.dumps(jsonObject)

@app.route('/nuclear/', methods=['POST'])
def nuclear():
    if request.method == 'POST':
        global jsonObject
        jsonObject = request.get_json()
        jsonObject['nuclear'] += 1
        jsonObject['Money'] -= input_to_ghg_map['nuclear']*10
        jsonObject = update_climate(jsonObject)
        return json.dumps(jsonObject)

@app.route('/solar/', methods=['POST'])
def solar():
    if request.method == 'POST':
        global jsonObject
        jsonObject = request.get_json()
        jsonObject['solar'] += 1
        jsonObject['Money'] -= input_to_ghg_map['solar']*10
        jsonObject = update_climate(jsonObject)
        return json.dumps(jsonObject)

@app.route('/fossil/', methods=['POST'])
def fossil():
    if request.method == 'POST':
        global jsonObject
        jsonObject = request.get_json()
        jsonObject['fossil'] += 1
        jsonObject['Money'] -= input_to_ghg_map['fossil']*10
        jsonObject = update_climate(jsonObject)
        return json.dumps(jsonObject)

if __name__ == "__main__":
    app.run(debug=True)

