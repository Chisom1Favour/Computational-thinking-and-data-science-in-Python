class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Plain - might change
        self._balance = balance     # private - need control
        self._transactions = 0      # internal counter

    @property
    def balance(self):
        print(f"Balance checked")
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Can't go negative")
        self._transactions += 1
        self._balance = amount

    @property
    def transactions(self):
        return self._transactions
    
    @property
    def is_overdrawn(self):
        return self._balance < 0
    
acc = BankAccount("Ada", 1000)
acc.balance = 5000
print(acc.balance)
print(acc.transactions)
print(acc.is_overdrawn)
