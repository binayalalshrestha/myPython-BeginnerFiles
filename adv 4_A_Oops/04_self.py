class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary for the employee working in {self.company} is {self.salary:,}\n{signature}")
    
    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee()
harry.salary=1_00_000
harry.getSalary("Thank You !!") #Employee.getSalary(harry)
harry.greet()


binay = Employee()
binay.salary=1_00_000_000
binay.getSalary("I am rich!")

