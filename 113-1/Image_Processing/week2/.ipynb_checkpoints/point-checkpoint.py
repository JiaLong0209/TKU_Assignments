import math

class Position: 
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


class Point:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
        self.length = self.get_length()

    def get_length(self):
        return math.sqrt(self.pos.x ** 2 + self.pos.y ** 2)

    def distance(self, point):
        return math.sqrt((self.pos.x - point.pos.x**2) + (self.pos.y - point.pos.y)**2)

    def info(self):
        print(f"value:{self.value} (x:{self.pos.x}, y:{self.pos.y}) ")
