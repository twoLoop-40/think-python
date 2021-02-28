from book import Point, Rectangle
import math
import copy

class Circle():
    '''
    Attributes
    center : Point
    radius : float
    '''

def distance_between(p1, p2):
    dx = abs(p1.x - p2.x)
    dy = abs(p1.y - p2.y)
    return math.sqrt(dx**2 + dy**2)

def point_in_circle(point, circle):
    center = circle.center
    radius = circle.radius

    if distance_between(point, center) <= radius:
        return True
    else:
        return False

def circle_in_rect(rect, circle):
    corner = rect.corner
    corner_x = corner.x 
    corner_y = corner.y 
    width = rect.width
    height = rect.height

    center = circle.center
    center_x = center.x 
    center_y = center.y 
    radius = circle.radius

    left = center_x - radius
    right = center_x + radius
    up = center_y + radius
    bottom = center_y - radius

    if (left >= corner_x and right <= corner_x + width and
        up <= corner_y + height and bottom >= corner_y):
        return True
    
def left_bottom(rect):
    return copy.copy(rect.corner)
def right_bottom(rect):
    corner = copy.copy(rect.corner)
    corner.x = corner.x + rect.width
    return corner
def left_up(rect):
    corner = copy.copy(rect.corner)
    corner.y += rect.height
    return corner
def right_up(rect):
    corner = copy.copy(rect.corner)
    corner.x += rect.width
    corner.y += rect.height
    return corner

def rect_in_circle(rect, circle):
    
    lb = left_bottom(rect)
    rb = right_bottom(rect)
    lu = left_up(rect)
    ru = right_up(rect)
    if point_in_circle(lb,circle) and point_in_circle(rb, circle) and point_in_circle(lu, circle) and point_in_circle(ru, circle):
        return True
    else:
        return False



    

