# marks1 = [45, 78, 86, 77]
# percentage1 = (sum(marks1)/len(marks1*100)*100)
# marks2 = [47, 68, 63, 56]
# percentage2 = (sum(marks2)/len(marks2*100)*100)
# print(percentage1, percentage2)

def p(marks):
    p = (sum(marks)/len(marks*100)*100)
    return p

marks1 = [45, 78, 86, 77]
percentage1 = p(marks1)
marks2 = [47, 68, 63, 56]
percentage2 = p(marks2)
print(percentage1, percentage2)


# quick quiz:
# write a program to greet a user with "Good day" using functions.

def greet(user):
    print("Good Day "+user)
greet("Binay")



#####
def mySum(num1, num2):
    return num1 + num2

s = mySum(5, 10)
print(s)

#####
def greet(name):
    gr = "Hello "+name
    return gr

a = greet("Binaya")
print(a)