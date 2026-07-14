class Food:
    def __init__(self, calories):
        self._calories = calories
    @property
    def calories(self):
        return self._calories

new = Food(30)
print(new.calories)
new.calories = 50