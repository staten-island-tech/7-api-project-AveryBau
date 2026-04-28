import requests
import json

def getMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)

""" {
    "data": [
    "0": "Mother cats teach their kittens to use the litter box.",
    "1": "A cat can sprint at about thirty-one miles per hour."
    ]
} """

fact = getMeow
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
