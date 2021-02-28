from time_transform import int_to_time, time_to_int 
import math

class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def time_to_int(self):
        return time_to_int(self)

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

class Point:
    '''
    point in 2D
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        return 'x 좌표: %g, y 좌표: %g' %(self.x, self.y)
    
if __name__ == '__main__':
    point = Point(3, 4)
    print(point)

