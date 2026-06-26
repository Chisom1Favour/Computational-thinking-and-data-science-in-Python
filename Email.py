class User:
    def __init__(self, email_address):
        self._email_address = email_address
    @property
    def email_address(self):
        return self._email_address
    @property
    def email(self):
        warnings.warn("Use .email_adress instead", DeprecationWarning)
        return self._email_address
    @email.setter
    def email(self, value):
        warnings.warn("Use .email_address instead", DeprecationWarning)
        self._email_address = value   
    