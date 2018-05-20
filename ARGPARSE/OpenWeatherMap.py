#!/Users/kevinmcgarry/venvs/openweather/bin/python
# the above path is used so that the venv doesn't have to be activated for the script to work

# Pre-requisites
# need an api key from openweathermap.org and store in env variable called OWM_API_KEY
# pip install requests module within the openweather venv


# Usage: weather.py zip_code --country country_code


import os
import requests
import sys

from argparse import ArgumentParser

parser = ArgumentParser(description='Get the current weather information')
parser.add_argument('zip', help='zip/postal code to get the weather for')
parser.add_argument('--country', default='us', help='country zip/postal belongs to, default is "us"')

args = parser.parse_args()

api_key = os.getenv('OWM_API_KEY')

# if there is no value assigned to the api_key
if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res = requests.get(url)

if res.status_code != 200:
    print(f"Error talking to weather provider: {res.status_code}")
    sys.exit(1)

weather_stats = res.json()
current_weather = weather_stats['weather'][0]['description']

print(f"Current Weather: {current_weather}")