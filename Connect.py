class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        print(f"Balance checked")
        return self._balance
    @property
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be zero")
        self._transactions += 1
        self._balance = amount
    @property
    def transactions(self):
        return self._transactions
    @property
    def is_overdrawn(self):
        return self._balance < 0

acc = BankAccount("Ada", 1000)
acc.balance = 500
print(acc.balance)
print(acc.transactions)
print(acc.is_overdrawn)