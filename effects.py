import random

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
   if ghg_temp_val>=0:
       ghg_fraction = 1.0 * ghg_temp_val/ghg_max_pos_val
   else:
       ghg_fraction = 1.0 * ghg_temp_val/ghg_max_neg_val
   return (ghg_temp_val,ghg_fraction)

#------------------

GHG = 0.5

nucSpent = 20000
fossilSpent = 10000
solSpent = 30000
windSpent = 25000
degree = 1000000

investment_dict = {}
investment_dict['Solar_Investment'] = solSpent
investment_dict['Wind_Investment'] = windSpent
investment_dict['Nuclear_Investment'] = nucSpent
investment_dict['Fossil_Investment'] = fossilSpent

input_to_ghg_map = {}
input_to_ghg_map['Solar_Investment'] = -0.5
input_to_ghg_map['Wind_Investment'] = -0.3
input_to_ghg_map['Nuclear_Investment'] = -0.2
input_to_ghg_map['Fossil_Investment'] = 1.0

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
	return carbon/4 - .2
	# adds to economy growth

def ecoCalc(carbon, sSpent, wSpent, nSpent, fSpent):
	x = random.random()
	totalSpent = sSpent + wSpent + nSpent + fSpent
	carbon += totalSpent/degree + x
	return carbon/2 - .2
	# defines economic growth


print(hurCalc(GHG))
print(ACCalc(GHG, nucSpent, fossilSpent))
print(agriCalc(GHG, fossilSpent))
print(ecoCalc(GHG, solSpent, windSpent, nucSpent, fossilSpent))
print(update_ghg(investment_dict, input_to_ghg_map))