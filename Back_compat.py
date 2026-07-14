"""Rename attributes without breaking old code"""

class Food:
    def __init__(self, name, cals):
        self.name = name
        self._cals = cals

@property
def calories(self):
    return self._cals

items = Food("Apple", 40)
print(items.calories)
