class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.height * self.width
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
r = Rectangle(4, 5)
print(r.area)
print(r.perimeter)
p = Rectangle(10, 20)
print(p.area)
print(p.perimeter)