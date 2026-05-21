import requests
from tkinter import *
import tkinter as tk 

def getMeow():
    Fact = Enter.get
    get = requests.get(f"https://meowfacts.herokuapp.com/?id={Fact()}")
    if get.status_code != 200:
        ResponseFact.config(text = "Error fetching data!")
    else:
        data = get.json()
        ResponseFact.config(text=f"Fact:{data["data"]}", bg = "lightblue", fg="black")

    
window = tk.Tk()
window.geometry("1000x1000")
window.title("Meow Facts")
window.resizable(True, True)


prompt = tk.Label(window, text="Hello! Do you wanna learn factz about catz? Type a number 0-91", font=("Arial", 20))
prompt.pack(pady=20, padx=10)

Enter = tk.Entry(window, font=("Arial", 20))
Enter.pack(pady=20, padx=10)

ResponseFact = tk.Label(window, text="", font=("Arial", 20), anchor='center', wraplength=700, justify="center")
ResponseFact.pack(pady=20, padx=10)

button = tk.Button(window, text="Enter", font=("Arial", 20), command=getMeow) 
button.pack(pady=10, padx=10)

window.mainloop()

