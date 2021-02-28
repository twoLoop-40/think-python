import turtle
import tkinter as tk

root = tk.Tk()

mt = turtle.Turtle()

def draw_poly(t, length, side):
    for i in range(side):
        t.fd(length)
        t.lt(360/side)
    
    
draw_poly(mt, 10, 50)

root.mainloop()
