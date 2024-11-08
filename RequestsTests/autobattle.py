import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'c8d31402fa3313db6a0ec32c9dbb3106'
TRAINER_ID = '7445'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
HEADER_NOTOKEN = {'Content-Type' : 'application/json'}
BODY_CREATE = {
    "name": "generate",
    "photo_id": -1
}

for i in range(20):
    try:
        try:
            response_new_id = requests.post(url = f'{URL}pokemons', headers = HEADER, json = BODY_CREATE )
            new_id = response_new_id.json()["id"]
            BODY_ADD = {"pokemon_id": new_id}
            requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = BODY_ADD )
        except:
            pass

        response_free_pok = requests.get(url = f'{URL}pokemons?in_pokeball=0&status=1&trainer_id={TRAINER_ID}')
        free_pok = response_free_pok.json()["data"][0]["id"]

        requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = {"pokemon_id": free_pok} )

        response_create = requests.get(url = f'{URL}pokemons?in_pokeball=1&status=1')
        enemy_id = response_create.json()["data"][6]["id"]
        print('Защищается', enemy_id)

        response_create_attack = requests.get(url = f'{URL}pokemons?in_pokeball=1&status=1&trainer_id={TRAINER_ID}')
        attack_id = response_create_attack.json()["data"][0]["id"]
        print('Атакует', attack_id)

        body_battle = {
            "attacking_pokemon": attack_id,
            "defending_pokemon": enemy_id
        }
        
        response = requests.post(url = f'{URL}battle', headers = HEADER, json = body_battle )
        print(response.text)

    except:
        continue