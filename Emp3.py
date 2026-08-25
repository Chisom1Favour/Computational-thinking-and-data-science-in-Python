class Customer:
    def __init__(self, first_name, last_name, email_address):
        self._first_name = first_name
        self._last_name = last_name
        self._email_address = email_address
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
    def email_address(self):
        return self._email_address.strip().lower()

c = Customer(" Emelie", "  Darlington ", "  CHICHI-@EMAIL.COM")
print(c.full_name)
print(c.email_address)