class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
r = Rectangle(4, 5)
print(r.area)
r.width = 10
print(r.perimeter)