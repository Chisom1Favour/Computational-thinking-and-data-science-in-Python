class Employee:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name.strip().title()

employee = Employee("  corra  ")
print(employee.name)