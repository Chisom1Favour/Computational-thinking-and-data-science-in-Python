class Circle:
    def __init__ (self, radius):
        self.radius = radius
    @property
    def area(self):
        return 3.14159 * self.radius ** 2
    
class Square:
    def __init__(self, side):
        self.side = side
    @property
    def area(self):
        return self.side ** 2
    
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    @property
    def area(self):
        return 0.5 * self.base * self.height
    
shapes = [Circle(3), Square(4), Triangle(6, 8)]
total = sum(s.area for s in shapes)