class Father:
    def father_method(self):
        print("Father class")

class Mother:
    def mother_method(self):
        print("Mother class")

class Child(Father, Mother):
    def child_method(self):
        print("Child class")

obj = Child()
obj.father_method()
obj.mother_method()
obj.child_method()