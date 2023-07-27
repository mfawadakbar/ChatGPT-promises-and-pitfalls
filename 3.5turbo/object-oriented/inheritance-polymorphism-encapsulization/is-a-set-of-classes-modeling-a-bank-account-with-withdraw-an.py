class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def __str__(self):
        return f"Account: {self.account_number}, Balance: {self.balance}"


class MinimumBalanceAccount(BankAccount):
    def __init__(self, account_number, balance=0, minimum_balance=0):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Withdrawal amount exceeds available balance")
        else:
            super().withdraw(amount)
