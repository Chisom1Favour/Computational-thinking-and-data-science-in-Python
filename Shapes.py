class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
class Square:
    def __init__(self, side):
        self._side = side
    @property
    def area(self):
        return self._side ** 2
class Triangle:
    def __init__(self, base, height):
        self._base = base
        self._height = height
    @property
    def area(self):
        return 0.5 * self._base * self._height

shapes = [Circle(3), Square(2), Triangle(3, 5)]
total = sum(s.area for s in shapes)