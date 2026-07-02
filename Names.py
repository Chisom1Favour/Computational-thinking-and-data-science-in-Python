class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def full_name(self):
        return f'{self.first} {self.last}'
    @full_name.setter
    def full_name(self, value):
        first, *last = value.split()
        self.first = first
        self.last = " ".join(last)


p = Person("ADA", "LOVELACE")
p.full_name = "Grace Hopper"
print(p.first)