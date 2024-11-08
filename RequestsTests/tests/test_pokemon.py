import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'c8d31402fa3313db6a0ec32c9dbb3106'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '7445'

def test_status_code():
    response = requests.get(url=f'{URL}trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_name():
    response_get = requests.get(url=f'{URL}trainers', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Енот Компот'