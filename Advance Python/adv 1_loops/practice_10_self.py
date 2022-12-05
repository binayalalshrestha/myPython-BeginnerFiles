username = 'binay'
password = 'binay'

con = 'y'

count = 1

while count <= 3 and con == 'y':

    usn = str(input("Enter username : \n"))
    pwd = str(input("Enter password : \n"))


    if usn == username and pwd == password:
        print ("User log-in successful! Welcome "+ username )
        print (f"Hello! Welcome to the program!!")
        dict1 = {
            '1' : 'Prime numbers upto the number 15',
            '2' : 'Ask if a certain number is Prime or not',
            '3' : 'Multiplication table of a number of your choice',
            '4' : 'The national flag of Nepal drawn by stars'
        }
        for key, value in dict1.items():
            print (key, ' : ', value)
        print ("Let's give you the list of all the prime numbers upto the number 15 first!!")
        for i in range ( 1, 16):
            count = 0  
            for j in range ( 2, i):
                if i % j == 0:
                    count = count + 1
                    break
            if count == 0:
                print(i, "is a prime number")

        print (f"You can also ask if a certain number is prime or not, but only one entry allowed!!")
        num = int(input("Enter a number : \n"))
        prime = True
        for i in range ( 2, num):
            if (num % i == 0):
                prime = False
                break
        if prime:
            print(f"{num} is a prime number")
        else:
            print("The number you have entered is not a prime number.")

        print (f" Now let's give you the multiplication table of your number of choice!!")
        urnum = int(input("Enter a number : \n"))
        for i in range (1, 11):
            print(f"{urnum} x {i} = {urnum * i}")

        

        stars = " * "
        for i in range ( 1, 6):
            print ( i * stars )
        stars2 = " * "
        for i in range ( 1, 6):
            print ( i * stars2 )
        print(' *')
        print(' *')
        print(' *')
        print(f" Here you have the national flag of Nepal drawn with the stars. ")

        break
    
    else:
        count = count + 1
        print ("Error! Username or password do not match credentials!")
        if con != str(input("Do you want to continue(y/n)")):
            break

