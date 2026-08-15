class Food:
    def __init__(self, name, calories, price):
        self.name = name
        self._calories = calories
        self._price = price

    @property
    def calories(self):
        return self._calories
    # SETTER: Controls write. Add validation/logic here
    @calories.setter
    def calories(self, value):
        if value < 0:
            raise ValueError("No negative calories")
        self._calories = value

    @property
    def calories_per_dollar(self):
        return self._calories / self._price
    @property
    def id(self):
        return hash(self.name)

a = Food("Apple", 50, 0.50)
a.Food = 100
print(a.calories)
print(a.calories_per_dollar)
# a.id = 123