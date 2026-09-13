class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price}")

    def apply_discount(self, percentage):
        discount = self.price * percentage / 100
        self.price -= discount

    def change_price(self, new_price):
        self.price = new_price

    def compare_price(self, other_book):
        if self.price > other_book.price:
            print(f"{self.title} is more expensive than {other_book.title}")
        elif self.price < other_book.price:
            print(f"{self.title} is cheaper than {other_book.title}")
        else:
            print(f"{self.title} and {other_book.title} have the same price")


book1 = Book("Atomic Habits", "James Clear", 600)
book2 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 450)
book3 = Book("The Power of Habit", "Charles Duhigg", 550)

books = [book1, book2, book3]

for book in books:
    book.display_info()
    print()

book1.apply_discount(10)
book2.apply_discount(20)

book3.change_price(700)

print("After Changes")
print()

for book in books:
    book.display_info()
    print()

book1.compare_price(book2)
book2.compare_price(book3)
book3.compare_price(book1)
