import tkinter as tk
from tkinter import *
import pygame
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
    root = Tk()

    def veryhigh():
        volume = 1
        pygame.mixer.music.set_volume(volume)

    def high():
        volume = 0.75
        pygame.mixer.music.set_volume(volume)


    def medium():
        volume = 0.5
        pygame.mixer.music.set_volume(volume)

    def low():
        volume = 0.25
        pygame.mixer.music.set_volume(volume)


    def novolume():
        volume = 0
        pygame.mixer.music.set_volume(volume)


    root.title("Options")

    frame = tk.Frame(root, bg="green")
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="yellow")
    frame.place(relx=0, rely=0, relwidth=0.66666, relheight=1)

    frame = tk.Frame(root, bg="red")
    frame.place(relx=0, rely=0, relwidth=0.33333, relheight=1)

    L = Label(root, text="Options Menu", font=("Ariel", 20, "bold", "underline"))
    L.pack()

    button = tk.Button(root, text="Vey High Sound", command= veryhigh, width = 15 ,font=("verdana", 12))
    button.pack()

    button = tk.Button(root, text="High Sound", command= high, width = 15 ,font=("verdana", 12))
    button.pack()

    button = tk.Button(root, text="Medium Sound", command = medium, width = 15 ,font=("verdana", 12))
    button.pack()

    button = tk.Button(root, text="Low Sound", command = low, width = 15 ,font=("verdana", 12))
    button.pack()

    button = tk.Button(root, text="No Sound",command = novolume, width = 15 ,font=("verdana", 12))
    button.pack()

    root.mainloop()


def button_event5():
    quit()


root = Tk()
root.title('Connect 4 Game')

frame = tk.Frame(root, bg="green")
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="yellow")
frame.place(relx=0, rely=0, relwidth=0.66666, relheight=1)

frame = tk.Frame(root, bg="red")
frame.place(relx=0, rely=0, relwidth=0.33333, relheight=1)

L = Label(root, text="3 Player Connect 4!!!",font=("Ariel",30,"bold", "underline"))
L.pack()

picture = tk.PhotoImage(file = "guipic.png")
img = Label(root, image = picture)
img.pack()

button = tk.Button(root, text="3 Player Game", command=button_event1, width = 15 ,font=("verdana", 12))
button.pack()

button = tk.Button(root, text="2 Player Game", command=button_event2, width = 15 ,font=("verdana", 12))
button.pack()

button = tk.Button(root, text="1 Player Game", command=button_event3, width = 15 ,font=("verdana", 12))
button.pack()

button = tk.Button(root, text="Options", command=button_event4, width = 15 ,font=("verdana", 12))
button.pack()

button = tk.Button(root, text="QUIT", command=button_event5, width = 15 ,font=("verdana", 12))
button.pack()

root.mainloop()




