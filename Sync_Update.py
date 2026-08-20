class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self.radius

c = Circle(5)
print(c.area)
c.radius = 10
print(c.area)