from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import csv

poke_dict = []

def export_csv(poke_dict):
	with open("poke_dict.csv", "w") as file:
		pokemon_writer = csv.writer(file)
		pokemon_writer.writerows(poke_dict)

def get_pokemon_names():

	# Reaching the page and getting HTML entities
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers={'User-Agent':user_agent,}
	url = Request("https://pokemondb.net/pokedex/national", None, headers)
	html = urlopen(url)

	# Converting into a BeautifulSoup object and iterating the content
	soup = BeautifulSoup(html.read(), "html5lib")
	
	for span in soup.findAll('span', attrs={'class':'infocard-lg-data'}):

		pokevariable = [] # Group up id and name 

		for pokeid in span.find('small'):
			# Pokemon ID, originally comes with #
			pokevariable.append(pokeid.split('#')[1])

		for name in span.findAll('a', attrs={'class':'ent-name'}):
			# Pokemon Name
			pokevariable.append(name.text)

		poke_dict.append(pokevariable)

if __name__ == '__main__':
	get_pokemon_names()
	export_csv(poke_dict)