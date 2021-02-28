import turtle

def koch(t, length, n):
    '''
    t : turtle
    length : length of koch curv
    n : how many segments
    '''

    if n == 0 :
        t.fd(length)
    else:
        koch(t, length/3, n-1)
        t.lt(60)
        koch(t, length/3, n-1)
        t.rt(120)
        koch(t, length/3, n-1)
        t.lt(60)
        koch(t, length/3, n-1)

if __name__ == '__main__':
    bob = turtle.Turtle()

    length = 400
    times = 5

    koch(bob, length, times)
    turtle.mainloop()
