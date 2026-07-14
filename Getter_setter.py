class Food:
    def __init__(self, calories):
        self._calories = calories
    @property
    def calories(self):
        return self._calories
    @calories.setter
    def calories(self, value):
        if value < 0:
            raise ValueError("Calories can't be negative")
        self._calories = value
    @calories.deleter
    def calories(self):
        del self._calories


apple = Food(90)
print(apple.calories)
apple.calories = 100
print(apple.calories)
del apple.calories