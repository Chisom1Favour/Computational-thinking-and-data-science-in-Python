"""Return the clean version of internal data"""

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name.title()
    
    @property
    def name_slug(self):
        return self._name.lower().replace(" ", "-")
    
p = Person("ada lovelace")
print(p.name)
print(p.name_slug)
