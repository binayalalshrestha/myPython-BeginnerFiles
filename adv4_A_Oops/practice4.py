# Add a static method in problem 2 to greet the
# user with hello.

class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    def squareRoot(self):
        print(f"The square root of {self.number} is {self.number **0.5}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number **3}")

    @staticmethod
    def greet():
        print("Hello User, here are your answers")
    
a = Calculator(3)
a.greet()
a.square()
a.squareRoot()
a.cube()
