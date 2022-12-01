## Write a program to print multiplication table of n using for loop in reversed order.

num=int(input("Enter the number \n"))
for table in range(1,11):
    i=11-table
    print(f"{num}X{i}={num*i}")


