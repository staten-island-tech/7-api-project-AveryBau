import requests
import json

def getMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/{cat.lower()}")
    if response.status_code != 100:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

fact = getMeow("")
print(fact)

""" def divide(a,b):
    try:
       result = a/b
    except ZeroDivisionError:
       print("Cannot divide by 0")
    else:
        print(a/b)


divide(10,0)
 """
