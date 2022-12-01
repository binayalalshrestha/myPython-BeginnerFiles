# Write a program using function to find the greatest of three numbers.

def gr(num1, num2, num3):
    if num1 > num2:
        # print (num1, "is greatest")
        return num1
    elif num2>num3:
        print (num2, "is greatest")
    elif num3>num1:
        print (num3, "is greatest")
a =gr(14,13,2)
print(a)


# def max(num1, num2, num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3

# m =max(4,2,6)
# print("The value of the greatest number is " + str(m))




