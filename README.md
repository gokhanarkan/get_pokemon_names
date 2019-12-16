# get_pokemon_names

Two different approaches on getting all the Pokemon names & their id's.

I needed Pokemon names in a list for a personal project but couldn't find on the web; so I decided to create myself.

I came up with ```get_pokenames_withapi.py``` first. However, it required an API call for every single Pokemon (around 800 calls!) and took about 15 minutes to finish. Then I realised the gen 8 was not even available in this database at all.

My second approach was even more straightforward; I found [this link](https://pokemondb.net/pokedex/national) where all the Pokemon details are listed already.

The second approach, ```get_pokenames_scraping.py```, only takes 2 seconds to get all the id's and names from this page and export them into a CSV file. Yes, 2 seconds.

I'm saving this code as a personal lesson to myself.

---

To run:
```pip install -r requirements.txt```

then,

```python get_pokenames_scraping.py```
