class Employee:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    @property
    def first_name(self):
        return self._first_name.strip().title()
    @property
    def last_name(self):
        return self._last_name.strip().title()
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

e = Employee(" Alih", "  Downing  ")
print(e.full_name)