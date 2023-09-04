from mastodon import Mastodon
from os import getenv
import json
import requests

api_base_url = getenv("API_BASE_URL"),
client_id = getenv("API_CLIENT_ID"),
client_secret = getenv("API_CLIENT_SECRET"),
access_token = getenv("API_ACCESS_TOKEN")

api = Mastodon(api_base_url = api_base_url,client_id = client_id,client_secret = client_secret,access_token = access_token)

def generate_toot():
    tweet=json.loads(requests.get('https://api.giratina.net/v1/raika').text)['text']
    return tweet

def run():  
    toot = generate_toot()
    api.status_post(status=toot, visibility="unlisted")
    
if __name__ == '__main__':
    run()

print("start")