class Employee:
    company = "Camel"
    salary = 100
    location = "Dehli"

    #dunder method
    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

print("\n")
e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary)
