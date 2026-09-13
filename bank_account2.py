class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self._balance:
            raise InsufficientBalanceError("Insufficient balance")

        self._balance -= amount

    def display_balance(self):
        print(f"{self.account_holder}: ₹{self._balance}")

    def calculate_interest(self):
        return 0


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self._balance * 0.04


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return self._balance * 0.02


savings = SavingsAccount("Rahul", 10000)
current = CurrentAccount("Priya", 15000)

accounts = [savings, current]

for account in accounts:
    account.display_balance()
    print("Interest:", account.calculate_interest())
    print()

try:
    savings.deposit(2000)
    savings.withdraw(3000)
    savings.display_balance()
except ValueError as error:
    print(error)
except InsufficientBalanceError as error:
    print(error)

try:
    current.withdraw(20000)
except ValueError as error:
    print(error)
except InsufficientBalanceError as error:
    print(error)

try:
    savings.withdraw(-500)
except ValueError as error:
    print(error)
except InsufficientBalanceError as error:
    print(error)