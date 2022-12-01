## Write a program to print multiplication table of a given number using

## (while loop)

num2 = int(input("Enter Number: \n"))
j = 1
print("The multiplication table of: ", num2)
while j <= 10:
    num2 = num2 * 1
    print(num2, 'x', j,'=',num2*j)
    j += 1