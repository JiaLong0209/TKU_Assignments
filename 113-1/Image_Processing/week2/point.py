class Position: 
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


class Point:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
    
    def info(self):
        print(f"value:{self.value} (x:{self.pos.x}, y:{self.pos.y}) ")


