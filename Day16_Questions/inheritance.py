# Question:
# Demonstrate inheritance using Parent and Child classes.
#
# Concept:
# Inheritance allows one class to use properties
# and methods of another class.

class Animal:

    def sound(self):
        print("Animal Makes Sound")


class Dog(Animal):

    def bark(self):
        print("Dog Barks")


d = Dog()

d.sound()

d.bark()