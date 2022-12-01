a = "Binay"
b = 10
c = 10.25
_d = ''' Shrestha'''

print("10 added to 10.25 is",b+c)
print("My name is",a+_d)
print(type(a),type(b),type(c))


# Operators in Python :
# Arithemetic Operators
d = 3
e = 2
print(d-e)

# Assignment Operators
f = 10
f += 5
f *= 3
print (f)

# Comparison Operators
g = (4>7)
h = (10==10)
i = (10!=5)
print(g)
print(h)
print(i)

# Logical Operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of bool1 not bool2 is", (not bool2))


# Type Casting
j = "40"
j = int(j)
print(type(j),(j + 10))


# Input Function

A = input("Enter your name : ")
print(A)