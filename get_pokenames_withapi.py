import requests, json, csv

poke_dict = [] # This will contain all the pokemon names after the script starts

# Getting individual pokemon names by their id with using pokeapi.
def get_pokemon_name(i): 
	request = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(i))
	try:
		if request.status_code == 200:
			rjs = json.loads(request.text)
			return rjs['forms'][0]['name']
		else: return False
	except: return False

# Exporting the list of pokemons into a csv file
def export_csv(poke_dict):
	with open("poke_dict_apiway.csv", "w") as file:
		pokemon_writer = csv.writer(file)
		pokemon_writer.writerows(poke_dict)

# Iterating all the ids to get pokemon names
i = 1
while(get_pokemon_name(i)):
	pokevariable = [i, get_pokemon_name(i)]
	poke_dict.append(pokevariable)
	i += 1

# At the end saving all data to csv file
export_csv(poke_dict)