import requests
import json

""" def getrandomMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/{cat.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    print(data)

fact = getrandomMeow("")
print(fact) """


""" def getmultipleMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/?count={cat.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    print(data)

fact = getmultipleMeow("3")
print(fact) """


""" def getspecificMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/?id={cat.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    print(data)

fact = getspecificMeow("1")
print(fact) """


""" def getlanguageMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/?lang={cat.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    print(data)

fact = getlanguageMeow("ukr")
print(fact) """