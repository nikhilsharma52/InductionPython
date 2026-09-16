class Parent:
    def display(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        print("Child class")

obj = Child()
obj.display()
obj.show()