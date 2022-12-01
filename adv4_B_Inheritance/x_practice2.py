'''
Create a class pets from a class Animals and
further create class Dog from pets. Add a method bark
to class Dog.
'''

class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color = "White"

class Dog(Pets):

    @staticmethod
    def bark():
        print("whoff whoff!!")

d = Dog()
d.bark()
print(d.animalType)