import requests
import json
import random
import tkinter
from tkinter import *
import tkinter as tk 

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





print("Hello! Do you wanna learn factz about catz?")
Userinput = input("What do you want to learn? Type any number.")
print(f"You chose fact number {Userinput}")


def getspecificMeow(cat):
    response = requests.get(f"https://meowfacts.herokuapp.com/?id={Userinput}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    print(data)

def meow_fact():
    text = entry.get()
    meow_text = text(f"{Userinput}")
    result_label.config(text = f"{meow_text}")
meow_fact
    
window = tk.Tk()
window.geometry("700x700")
window.title("Meow Facts")
window.resizable(True, True)


prompt = tk.Label(window, text="Hello! Do you wanna learn factz about catz? Type any number below:", font=("Arial", 14))
prompt.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14), width = 30)
entry.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=15)

button = tk.Button(window, text="Enter", font=("Arial", 14), command=meow_fact) 
button.pack(pady=10)

window.mainloop()

""" Title = Label(master = Window, text = "Meow Facts")
Title.pack()
Enter = Entry(master = Window)
Enter.pack

instruct = Label(master = Window, text = "What do you want to learn? Type any number.")
instruct.pack

Checked = Label(master = Window, text = "check")
Checked.pack 

Button1 = Button(master = Window, command = facts, text = "Type any number.")
Button1.pack

newMeow() """