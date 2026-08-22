class Employee:
    def __init__(self, name, employee_id, department):
        self._name = name
        self._employee_id = employee_id
        self._department = department
    @property
    def name(self):
        return self._name.strip().title()
    @property
    def employee_id(self):         # Read only
        return self._employee_id
    @property
    def department(self):
        return self._department.strip().title()
    

employee = Employee(
    "  John Doe  ",
    "221",
    " engineering  "
)
print(employee.name)
print(employee.employee_id)
print(employee.department)