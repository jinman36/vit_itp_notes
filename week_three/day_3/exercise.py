import openpyxl
import requests
import json
# make one api cal to retrieve the list of pokemon

####### get first pokemon from the api call
response  = requests.get("https://pokeapi.co/api/v2/pokemon")
json_data = json.loads(response.text)
first_pokemon = json_data['results'][0]




# append to a list thats going to hold all of the pokemon dictionaries with name and urls

#  iterate through eh list of pokemons
#  make subsequent api calls to retrieve abilities list

#### get the abilities for the first_pokemon

abilities_response = requests.get(first_pokemon['url'])
abilities_json_data = json.loads(abilities_response.text)
just_abilities_of_first_pokemon = abilities_json_data['abilities']

print(just_abilities_of_first_pokemon)


#  tranform abilities list in an excel compatible format

######### transform or stringify the abilities together
abilities_string = ""
for each_ability in just_abilities_of_first_pokemon:
  abilities_string += each_ability['ability']['name'] + ' '

print(abilities_string)
# write to excel

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = first_pokemon['name']
sheet['B1'] = abilities_string

wb.save('/mnt/c/Users/Jeffe/source/codefellows/vetsInTech/vit_itp_notes/week_four/day_2/output.xlsx')







