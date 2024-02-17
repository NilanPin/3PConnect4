import tkinter as tk
from tkinter import *

def button_event1():
    import ThreePlayers
    print(ThreePlayers)

def button_event2():
    import TwoPlayersGame
    print(TwoPlayersGame)


def button_event3():
    print("Clicked")

def button_event4():
    print("Clicked")

def button_event5():
    quit()

root = Tk()
root.title('3 Player Connect 4 Game')

canvas = tk.Canvas(root, height=100, width=100)
canvas.pack()

frame = tk.Frame(root, bg="yellow")
frame.place(relx=0, rely=0, relwidth=1, relheigh=1)

frame = tk.Frame(root, bg="green")
frame.place(relx=0, rely=0, relwidth=0.66666, relheigh=1)

frame = tk.Frame(root, bg="red")
frame.place(relx=0, rely=0, relwidth=0.33333, relheigh=1)

L = Label(root, text="Welcome to 3P Connect 4!!!",font=("Ariel",30,"bold", "underline"))
L.pack()

button = tk.Button(root, text="3 Player Game",font = 20, command=button_event1)
button.pack()

button = tk.Button(root, text="2 Player Game",font = 20, command=button_event2)
button.pack()

button = tk.Button(root, text="1 Player Game",font = 20, command=button_event3)
button.pack()

button = tk.Button(root, text="Options",font = 20, command=button_event4)
button.pack()

button = tk.Button(root, text="QUIT",font = 20, command=button_event5)
button.pack()

root.mainloop()

