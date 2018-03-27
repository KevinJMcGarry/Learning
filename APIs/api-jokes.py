"""
Script that asks the user for a search term and uses that term to query the 'icanhazdadjoke.com' api for a list
of jokes that contain that term. If more than one joke is found for the search term, a random one is selected and
displayed.

"""

import requests
import random


def search_joke(url, search_term):
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": search_term}  # check site api documentation for keys to use/that are valid
    )
    jokes = response.json()
    if len(jokes['results']) > 1:
        print(f"There were {len(jokes['results'])} jokes found for the term {search_term}")
        random_joke_obj = (random.choice(jokes['results']))
        random_joke = random_joke_obj['joke']
        print(f"your random joke is : \n\n{random_joke}")
    elif len(jokes['results']) == 1:
        print(f"Only one joke was found for the term {search_term}")
        print(jokes['results'][0]['joke'])
    else:
        print(f"There were no jokes for the term {search_term}")


search_term = input("please enter a joke topic: ")
search_joke("https://icanhazdadjoke.com/search", search_term)

# note the search_term is the equivalent of us typing in
# https://icanhazdadjoke.com/search?term='search_term'
