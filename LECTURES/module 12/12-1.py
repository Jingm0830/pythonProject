"""
Write a program that fetches and prints out a random Chuck Norris joke for the user.
Use the API presented here: https://api.chucknorris.io/.
The user should only be shown the joke text.
"""

import requests
url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url)
if response.status_code == 200:
    print(response.json()['value'])
else:
    print("null")