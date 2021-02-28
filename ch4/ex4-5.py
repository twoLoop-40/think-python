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
    i = 0
    while i < n:
        t.fd(length)
        t.lt(angle)
        i = i + 1




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

def spiral(t, ratio, angle, length):

    n = int(angle)
    startLength = length / n

    for i in range(n):
        arc(t, startLength * (ratio * i), angle / n)

if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a leaf
    l = 90.0
    angle = 360.0
    spiral(bob, 1.05, angle, l)

    # wait for the user to close the window
    turtle.mainloop()
