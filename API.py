import requests
import json

""" def getMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    print(data)

fact = getMeow("")
print(fact)
 """


def getMeow3(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/?count=3")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    print(data)

fact = getMeow3("")
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
