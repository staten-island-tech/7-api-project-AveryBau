import requests
import json
""" import random
import tkinter
from tkinter import *
 """
""" def getrandomMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/{cat.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    print(data)

fact = getrandomMeow("")
"""


""" def getmultipleMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/?count={cat.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    print(data)

fact = getmultipleMeow("3")"""


def getspecificMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/?id={cat.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    if getspecificMeow("1"):
        print(data)

""" def checking():
    if answers:
        guess = Enter.get()
        if guess in answers:
            Checked.config(text="Good job")
            answers.remove(guess)
        else: 
            Checked.config(text="NOo")
    else: 
        Checked.config(text="Congrats")
        newMeow()
    
def newMeow():
    New = random.choice()
    x = getspecificMeow(New)
    global answers
    answers = []
    for i in range(len(x)):
        answers.append(x[i][""])

    instruct.config(text = f"Can you learn cool, new facts about cats?")

Window = Tk()
Window.geometry("500x500")

Title = Label(master=Window, text = "Meow Facts")
Title.pack()
Enter = Entry(master=Window)
Enter.pack

instruct = Label(master=Window, text = "")
instruct.pack

Checked = Label(master=Window, text="check")
Checked.pack

Button1 = Button(master=Window, command= checking, text = "Guess")
Button1.pack

newMeow()

Window.mainloop() """