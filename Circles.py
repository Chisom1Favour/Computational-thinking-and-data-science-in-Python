class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def age(self):
        return 3.14159 * self.radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self.radius
    
c = Circle(10)
print(c.age)
print(c.circumference)