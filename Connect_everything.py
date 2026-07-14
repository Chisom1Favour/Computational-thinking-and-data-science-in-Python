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
            raise ValueError("Calorie can't be negative")
        self._calories = value

    @property
    def calories_per_dollar(self):
        return self._calories / self._price
    
    @property
    def id(self):
        return hash(self.name)  # computed ocne, never changes
    
apple = Food("apple", 100, 15)
print(apple.calories)
apple.calories = 150
print(apple.calories)
print(apple.calories_per_dollar)
print(apple.id)