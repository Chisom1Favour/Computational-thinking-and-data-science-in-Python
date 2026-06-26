class Food:
    def __init__(self, name, calories, price):
        self.name = name
        self._calories = calories
        self._price = price
    @property
    def calories(self):
        return self._calories
    @calories.setter
    def calories(self, value):
        if value < 0:
            raise ValueError("No negative calories allowed")
        self._calories = value
    @property
    def calories_per_dollar(self):
        return self._calories / self._price
    @property
    def id(self):
        return hash(self.name)
    
apple = Food("Pizza", 215, 300)
apple.calories = 900
print(apple.calories)
print(apple.calories_per_dollar)
apple.id = 123