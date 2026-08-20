class User:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must not be less than zero")
        self._age = value

u = User(13)
print(u.age)
u.age = -3