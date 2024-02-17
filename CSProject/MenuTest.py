import tkinter as tk
from tkinter import *
import pygame
from pygame import mixer
from pygame.examples.music_drop_fade import volume


mixer.init()
music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(volume)


def button_event1():
    import ThreePlayers


def button_event2():
    import TwoPlayer



def button_event3():
    import SinglePlayer




def button_event4():
    root = Tk()

    def high():
        volume = 1
        pygame.mixer.music.set_volume(volume)
        return volume

    def medium():
        volume = 0.5
        pygame.mixer.music.set_volume(volume)
        return volume

    def low():
        volume = 0.25
        pygame.mixer.music.set_volume(volume)
        return volume

    def novolume():
        volume = 0
        pygame.mixer.music.set_volume(volume)
        return volume

    root.title("Options")
    L = Label(root, text="Options Menu", font=("Ariel", 20, "bold", "underline"))
    L.pack()

    button = tk.Button(root, text="High Sound", command= high)
    button.pack()

    button = tk.Button(root, text="Medium Sound", command = medium)
    button.pack()

    button = tk.Button(root, text="Low Sound", command = low)
    button.pack()

    button = tk.Button(root, text="No Sound",command = novolume)
    button.pack()

    root.mainloop()


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



