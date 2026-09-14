class Grandparent:
    def grandparent_method(self):
        print("Grandparent class")

class Parent(Grandparent):
    def parent_method(self):
        print("Parent class")

class Child(Parent):
    def child_method(self):
        print("Child class")

obj = Child()
obj.grandparent_method()
obj.parent_method()
obj.child_method()