import requests
import json

def getFish(fish):
    response = requests.get(f"https://www.fisheries.noaa.gov/topic/sustainable-seafood{fish.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)
    types = []
    for t in data["types"]:
        types.append(t["type"]["name"])
    for key, value in seafood.items():
        print(key, "→", value)
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

seafood = getFish("Alaska Snow Crab")
print(seafood)
for key, value in seafood.items():
    print(f"{key.title()}: {value}")

