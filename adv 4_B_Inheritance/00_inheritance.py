class Employee:
    company = 'Google'

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    company = 'YouTube'
    language = 'Python'

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is a programmer")

e = Employee()
e.showDetails()
print(e.company)

p = Programmer()
p.showDetails()
print(p.company)
