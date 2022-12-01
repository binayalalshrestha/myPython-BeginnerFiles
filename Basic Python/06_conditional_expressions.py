# if-elif-else ladder in py
print("if-elif-else ladder in py")
a = 8
if(a<3):
    print("The value of a is greater than 3")
elif(a>13):
    print("The value of a is grater than 13")
elif(a>7):
    print("The value of a is grater than 7")
elif(a>17):
    print("The value of a is grater than 17")
else:
    print("The value is not grater than 3 or 7\n")
print(".\n")

# The space after the if() sentence is indentation
# It can be done with either [    ]4 Space buttons,
# Or a tab,
# Or VSCode does it itself.


## Multiple if statements
print("Multiple if statements")
a = 8
if(a<3):
    print("The value of a is less than 3")
if(a>13):
    print("The value of a is grater than 13")
if(a>7):
    print("The value of a is grater than 7")
if(a>17):
    print("The value of a is grater than 17")
else:
    print("The value is not grater than 3 or 7")
print("\n")

## Me trying out myself
myNum = 164
if(myNum > 165):
    print("True")
elif(myNum < 164):
    print("True")
elif(myNum >163):
    print("True")
else:
    print("Flase")


# Quick practice
print("practice 1\n")
a = int(input("Enter the age:\n"))
if(a==18):
    print("Yes")
elif(a>18):
    print("Yes")
else:
    print("The person is too young")
print("\n")

# [ Harry's method ]
# age = int(input("Enter age:"))
# if age>18:
#     print("Yes")
# else:
#     print("No")


# Quick practice 2
print("practice 2\n")
age = int(input("Enter your age:\n"))
if(age>34 and age<56):
    print("You can work with us")
else:
    print("You cannot work with")
print("\n")
weight = int(input("Enter your weight:\n"))
if(weight>=50 or weight==70):
    print("you can proceed")
else:
    print("your weight doesn't match our criteria")
print("\n")


# (is) and (in)

# (is)
aNum = None
if(aNum is None):
    print("Yes")
else:
    print("No")
print("\n")

# (in)
aList = [45, 56, 69]
print(365 in aList)#checks if the number is in the list or not.
print("\n")

# Notes : a. There can be any number of elif statements.
#         b. Last else if executed only if all the conditions inside elifs fail.