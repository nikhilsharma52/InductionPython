class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    @classmethod
    def from_name(cls, name):
        return cls(name, 18, "CSE")

    @classmethod
    def from_name_age(cls, name, age):
        return cls(name, age, "ME")

    @classmethod
    def from_full_details(cls, name, age, course):
        return cls(name, age, course)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student.from_name("Rahul")
student2 = Student.from_name_age("Priya", 20)
student3 = Student.from_full_details("Aman", 21, "Computer Science")

student1.display()
student2.display()
student3.display()
