from __future__ import print_function, division

import math
import turtle

def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def leaf(t, r, n, ol):
    """ Draws half of leaf 
    t : Turtle
    r : radius i.e size of leaf
    n : number of leaves
    ol : number of overlap
    """
    angle = 360.0 / n
    arc(t, r, angle)
    t.lt(180-angle)
    arc(t,r,angle)
    t.lt(180)
    t.rt(angle - angle/ol)



def flower(t, r, n, m):
    numberOfLeaf = n * m
    for i in range(numberOfLeaf):
        leaf(t, r, n, m)




if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a leaf
    radius = 200
    flower(bob, radius, 6, 2)


    # wait for the user to close the window
    turtle.mainloop()
