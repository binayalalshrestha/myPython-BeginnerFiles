class Employee:
    Company = "Google"
    Salary = 100

harry = Employee()
rajni = Employee()
harry.salary = 300
rajni.salary = 400
print(f"The salary of Harry is {harry.salary}")
print(f"The salary of Harry is {rajni.salary}")
## If salary is not given in instance than the program checks in class
