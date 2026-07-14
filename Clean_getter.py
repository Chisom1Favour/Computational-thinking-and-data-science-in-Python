class Food:
    def __init__(self, name, calories):
        self.name = name
        self._calories = calories
    @property
    def calories(self):
        print("Getting calories")
        return self._calories
    
apple = Food("Apple", 30)
print(apple.name)
print(apple.calories)