import os
import requests


API_BASE_URL = 'https://br1.api.riotgames.com/lol/'
SUMMONER_ENDPOINT = 'summoner/v4/summoners/by-name/'
RANKED_STATS_ENDPOINT = 'league/v4/entries/by-summoner/'

API_KEY = os.environ['API_KEY']

summoner = 'kami'
summoner_url = f'{API_BASE_URL}{SUMMONER_ENDPOINT}{summoner}?api_key={API_KEY}'

response = requests.get(summoner_url)
summoner_info = response.json()
print(summoner_info)

summoner_id = summoner_info.get('id') 
ranked_url = f'{API_BASE_URL}{RANKED_STATS_ENDPOINT}{summoner_id}?api_key={API_KEY}'

response = requests.get(ranked_url)
ranked_info = response.text
print(ranked_info)
