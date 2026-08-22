class Employee:
    def __init__(self, first_name, last_name, hire_date):
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._status = "active"
        self._salary = 250000
        
    @property
    def first_name(self):
        return self._first_name.strip().title()
    @property
    def last_name(self):
        return self._last_name.strip().title()
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    @property
    def years_of_service(self):
        return self._hire_date
    @property
    def is_active(self):
        return self._status == "active"
    @property
    def salary(self):
        return self._salary
    @property
    def display_salary(self):
        return f"#{self._salary:,.2f}"

e = Employee(" Alih", "  Downing  ", "June 1990")
print(e.full_name)
print(e.is_active)
print(e.years_of_service)
print(e.salary)
print(e.display_salary)