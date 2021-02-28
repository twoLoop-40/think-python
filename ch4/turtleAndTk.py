import turtle
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(master=root, width=500, height=500)
canvas.pack()

t = turtle.RawTurtle(canvas)

tk.Button(master=root, text="Forward", command=lambda: t.forward(100)).pack(side=tk.TOP)
tk.Button(master=root, text="Back", command=lambda: t.back(100)).pack(side=tk.BOTTOM)
tk.Button(master=root, text="Left", command=lambda: t.left(90)).pack(side=tk.LEFT)
tk.Button(master=root, text="Right", command=lambda: t.right(90)).pack(side=tk.RIGHT)

root.mainloop()