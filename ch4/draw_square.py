import turtle 

def square(t):
    for i in range(4):
        t.fd(200)
        t.lt(90)
    
tu = turtle.Turtle()

square(tu)
turtle.mainloop()


