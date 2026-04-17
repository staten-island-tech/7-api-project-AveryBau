import requests

def getPoke(poke):
    response =
requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")