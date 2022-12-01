#Write a program to print the following star pattern

#        *
#      * * *
#    * * * * *         for n = 3

n = 3
for i in range(3):                  #   i range ( 3 - 1 ) [2]
    print(" " * (n-i-1), end="")    #   " " * 2 ( two blanks)
    print("*" * (2*i+1), end="")    #   * x 2 *
    print(" " * (n-i-1))            #   
