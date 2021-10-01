import requests
from pprint import pprint
username = "sid86-dev"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()

pprint(user_data)
pprint(user_data['followers'])