class User(db.Model):
    _email_address = db.column('email_address', db.String)
    @property
    def email_address(self):
        return self._email_address
    @property
    def email(self):
        return self._email_address
    @email.setter
    def email(self, value):
        self._email_address = value
    