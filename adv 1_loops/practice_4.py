## Write a program to find whether a given number is prime or not.

num = int(input('Enter the number: \n'))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is a prime number")
else:
    print("This number is not a prime number")