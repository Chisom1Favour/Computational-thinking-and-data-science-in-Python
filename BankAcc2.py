class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self._transactions = 0
    
