class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing...")

class Programmer(Employee):
    company = "Fiver"

    def getSalary(self):
        print(f"No salary for programmers")

    def takeBreath(self):
        print("I am a Programmer so I am luckily breathing + +...")

p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()
print(e.country)

pr = Programmer()
pr.takeBreath()
print(f"The programmer is from {pr.country}")