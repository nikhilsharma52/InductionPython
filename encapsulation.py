class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current balance:", self.__balance)

    def get_account_details(self):
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance)


account = BankAccount("Rahul", "123456789", 5000)

account.get_account_details()
account.deposit(2000)
account.withdraw(1500)
account.check_balance()
