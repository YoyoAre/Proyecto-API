import requests
import random

api1 = 'https://fakerapi.it/api/v1/persons?_quantity=1'
api2 = f'https://pokeapi.co/api/v2/pokemon/{random.randint(1,151)}'
api3 = 'https://api.chucknorris.io/jokes/random'

r1 = requests.get(api1)
r1 = r1.json()["data"][0]

persona = r1["firstname"] + " " + r1["lastname"]

r2 = requests.get(api2).json()
pokemon = r2["name"]

r3 = requests.get(api3).json()
chuck = r3["value"]

print(f'{persona} su pokemon favorito es {pokemon} y su frace favorita es "{chuck}"')
