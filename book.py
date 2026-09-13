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
        self.price -= self.price * percentage / 100


book1 = Book("The Alchemist", "Paulo Coelho", 300)
book2 = Book("1984", "George Orwell", 400)
book3 = Book("Harry Potter", "J.K. Rowling", 500)

books = [book1, book2, book3]

for book in books:
    book.display_info()
    print()

book1.apply_discount(10)
book2.apply_discount(20)

print("After Discount")
print()

for book in books:
    book.display_info()
    print()
