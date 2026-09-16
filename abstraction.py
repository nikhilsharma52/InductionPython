from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def payment_status(self):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")

    def payment_status(self):
        print("Payment successful")


class UPI(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")

    def payment_status(self):
        print("Payment successful")


class Cash(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Cash")

    def payment_status(self):
        print("Payment successful")


credit_card = CreditCard()
upi = UPI()
cash = Cash()

credit_card.pay(2000)
credit_card.payment_status()

upi.pay(1500)
upi.payment_status()

cash.pay(500)
cash.payment_status()
