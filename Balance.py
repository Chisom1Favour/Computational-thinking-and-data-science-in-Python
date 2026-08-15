class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        print(f"[LOG] Balance accessed: {self._balance}")
        return self._balance

acc = BankAccount(5000)
print(acc.balance)