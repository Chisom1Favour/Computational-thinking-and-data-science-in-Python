"""Make different classes feel the same"""

class Circle:
    def __init__(self, radius):
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
    
shapes = [Circle(3), Square(4)]
for s in shapes:
    print(s.area)