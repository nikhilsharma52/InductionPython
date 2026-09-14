class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(self.name, "makes a sound")


class Dog(Animal):
    def sound(self):
        print(self.name, "barks")


class Cat(Animal):
    def sound(self):
        print(self.name, "meows")


class Cow(Animal):
    def sound(self):
        print(self.name, "moos")


animals = [
    Dog("Jackie"),
    Cat("Tom"),
    Cow("Bill")
]

for animal in animals:
    animal.sound()
