class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name.title()
    @property
    def name_slug(self):
        return self._name.lower().replace(" ", "-")
    
a = Person("Ada")
print(a.name)
print(a.name_slug)