import requests

token = 'c45ebca60b0ac5a8b0f7ad8193a3d8e7'

response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "Пухляш",
    "photo": "https://dolnikov.ru/pokemons/albums/018.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})


response = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "6248",
    "name": "Хрустяш",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

response = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "6248",
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response.text)