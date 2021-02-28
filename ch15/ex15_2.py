import turtle
import copy

ninja = turtle.Turtle()
class Point:
    '''
    point in 2D
    '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
class Rect:
    def __init__(self, corner = Point(0, 0), width=0, height=0):
        self.corner = corner
        self.width = width
        self.height = height
    
    def lb(self):
        return copy.copy(self.corner)
    def rb(self):
        corner = copy.copy(self.corner)
        corner.x += self.width
        return corner
    def lu(self):
        corner = copy.copy(self.corner)
        corner.y += self.height
        return corner
    def ru(self):
        corner = copy.copy(self.corner)
        corner.x += self.width
        corner.y += self.height
        return corner

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    
def draw_rect(tu, rect):
    '''
    tu : turtle.Turtle
    rect : Rect
    '''
    dir_x = rect.width
    dir_y = rect.height
    def move():
        tu.fd(dir_x)
        tu.lt(90)
        tu.fd(dir_y)
        tu.lt(90)
    
    def double(func, times=1):
        while times > 0:
            func()
            times -= 1
    
    double(move, 2)

def draw_circle(tu, circle):
    r = circle.radius
    tu.pu()
    tu.fd(r)
    tu.lt(90)
    tu.pd()
    tu.circle(r)




if __name__ == '__main__':
    jh = turtle.Turtle()
    spoint = Point(10, 10)
    rect = Rect(spoint, 200, 100)
    circle = Circle(spoint, 200)


    draw_rect(jh, rect)
    draw_circle(jh, circle)

    turtle.mainloop()





    

