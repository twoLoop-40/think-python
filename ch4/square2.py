import turtle
import tkinter as tk

root = tk.Tk()

mt = turtle.Turtle()

def draw_sq(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    
draw_sq(mt, 200)

root.mainloop()
