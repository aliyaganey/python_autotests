import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = 'c45ebca60b0ac5a8b0f7ad8193a3d8e7'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id': 2038})
    assert response.status_code == 200