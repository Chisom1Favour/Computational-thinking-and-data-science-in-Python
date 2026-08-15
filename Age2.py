class User:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if age < 0:
            raise ValueError("Age must not be less than zero")
        return self._age 