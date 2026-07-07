import time


class BankAccount:
    def __init__(self, name, amount, pin):
        self.name = name
        self._amount = amount
        self._pin = pin
        self._account_id = time.time()

    @property
    def account_id(self):
        return self.name + _account_id

    @property
    def balance(self):
        return self._amount
    @balance.setter
    def balance(self, value):
        if value <= 0:
            raise ValueError("Can't be negative")
        self._amount = value
    @property
    def pin(self):
        return self._pin
    @pin.setter
    def pin(self, value):
        if len(str(abs(value))) != 4:
            raise ValueError("Must be 4 digits")
        self._pin = value
    @property
    def is_overdrawn(self):
        return False
    

acc = BankAccount("Ada", 1000, pin=1234)
acc.balance = 1500
# acc.balance = -150
print(acc.balance)

acc.pin = 9999
# acc.pin = 12

print(acc.account_id)
print(acc.is_overdrawn)
# acc.account_id = "hack"