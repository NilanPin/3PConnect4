import tkinter as tk
from tkinter import *
import pygame
import vol as vol
from pygame import mixer

mixer.init()
music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()



def button_event1():
    import ThreePlayers


def button_event2():
    import TwoPlayer



def button_event3():
    import SinglePlayer




def button_event4():
    print("")
    root = Tk()
    root.title("Options")
    L = Label(root, text="Options Menu", font=("Ariel", 20, "bold", "underline"))
    L.pack()

    button = tk.Button(root, text="High",vol = 1)
    button.pack()

    button = tk.Button(root, text="Medium", vol = 0.5)
    button.pack()

    button = tk.Button(root, text="Low", vol = 0.25)
    button.pack()



def button_event5():
    quit()

root = Tk()
root.title('Connect 4 Game')

#canvas = tk.Canvas(root, height=100, width=100)
#canvas.pack()

frame = tk.Frame(root, bg="green")
frame.place(relx=0, rely=0, relwidth=1, relheigh=1)

frame = tk.Frame(root, bg="yellow")
frame.place(relx=0, rely=0, relwidth=0.66666, relheigh=1)

frame = tk.Frame(root, bg="red")
frame.place(relx=0, rely=0, relwidth=0.33333, relheigh=1)

L = Label(root, text="3 Player Connect 4!!!",font=("Ariel",20,"bold", "underline"))
L.pack()


button = tk.Button(root, text="3 Player Game", command=button_event1)
button.pack()

button = tk.Button(root, text="2 Player Game", command=button_event2)
button.pack()

button = tk.Button(root, text="1 Player Game", command=button_event3)
button.pack()

button = tk.Button(root, text="Options", command=button_event4)
button.pack()

button = tk.Button(root, text="QUIT", command=button_event5)
button.pack()


root.mainloop()

