import turtle
import math

def triangle(t, sideLength, angle):
    """ draw a triangle 
    t : turtle
    sideLength
    angle : central angle
    """
    sideAngle = 90.0 + angle/2
    radForAng = angle * math.pi / 180
    base = 2 * sideLength * math.sin(radForAng/2)
    t.fd(sideLength)
    t.lt(sideAngle)
    t.fd(base)
    t.lt(sideAngle)
    t.fd(sideLength)
    t.lt(180)

def pie(t, r, n):
    """
    t : turtle
    r : radius of which circle surround
    n : how many pie
    """
    angle = 360.0/n
    for i in range(n):
        triangle(t, r, angle)


if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a triangle 
    sl = 200
    pieces = 12
    pie(bob, sl, pieces)


    # wait for the user to close the window
    turtle.mainloop()

    

