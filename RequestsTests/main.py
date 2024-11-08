import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'c8d31402fa3313db6a0ec32c9dbb3106'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
HEADER_NOTOKEN = {'Content-Type' : 'application/json'}
BODY_CREATE = {
    "name": "generate",
    "photo_id": -1
}

response_new_id = requests.post(url = f'{URL}pokemons', headers = HEADER, json = BODY_CREATE )
new_id = response_new_id.json()["id"]

BODY_ADD = {"pokemon_id": new_id}
print(new_id)

requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = BODY_ADD )

BODY_RENAME = {
    "pokemon_id": new_id,
    "name": "Danny",
    "photo_id": -1
}

response_rename = requests.put(url = f'{URL}pokemons', headers = HEADER, json = BODY_RENAME )
print(response_rename.text)