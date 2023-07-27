Here is a Python script that implements the bank account classes as described:

```python
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
```

To test the classes, add the following code outside the class definitions:

```python
if __name__ == "__main__":
    account1 = BankAccount(12345, 1000)
    print(account1)
    account1.deposit(500)
    print(account1)
    account1.withdraw(200)
    print(account1)

    account2 = MinimumBalanceAccount(67890, 2000, 1000)
    print(account2)
    account2.deposit(500)
    print(account2)
    account2.withdraw(1500)
    print(account2)
```

Running the script should output the account details and perform some deposits and withdrawals.

Note: The script assumes that the user will input the account details and perform operations on the created account objects within the script itself rather than taking user input from the command line.