#!/usr/bin/env python

""" 
SYP Python Game pre production - Controlls

Controll for a simple dot on a simple window. This code uses Tkinter.
 """


from tkinter import *

# not sure what it does
root = Tk()
# adds title to the game window
root.title("Submarine Game Move Test")

# sets window size and sets origin to center.
w = 1280
h = 720
x = w//2
y = h//2

# calls canvas, creats window based on h, w.
game_canvas = Canvas(root, width=w, height=h, bg="white")
game_canvas.pack(pady=20)

# creates "character"
dot = game_canvas.create_oval(x, y, x+10, y+10,)

# defines the four movement directions, origin is center. Ties them to an even.
def move_left(event):
    x = -10
    y = 0
    game_canvas.move(dot, x, y)

def move_right(event):
    x = 10
    y = 0
    game_canvas.move(dot, x, y)

def move_up(event):
    x = 0
    y = -10
    game_canvas.move(dot, x, y)

def move_down(event):
    x = 0
    y = 10
    game_canvas.move(dot, x, y)


# defines events (key presses) 
root.bind("<a>", move_left)
root.bind("<d>", move_right)
root.bind("<w>", move_up)
root.bind("<s>", move_down)

# defines game mainloop
root.mainloop()