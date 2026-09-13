class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self._balance}")


account1 = BankAccount("Rahul", 5000)
account2 = BankAccount("Priya", 3000)

accounts = [account1, account2]

for account in accounts:
    account.display_balance()
    print()

account1.deposit(2000)
account1.withdraw(1500)
account1.withdraw(10000)

print()
account1.display_balance()
