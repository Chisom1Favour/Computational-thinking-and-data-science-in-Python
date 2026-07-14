"""Track when or why atrributes are read during development"""

class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    @property
    def balance(self):
        print(f"[LOG] Balance accessed: {self._balance}")
        return self._balance
    
b = BankAccount(1000)
print(b.balance)