# Write a recursive function to calculate the sum of
# first n natural numbers.

def recursion(k):
    if k <= 1:
       return k
    else:
  	    return k + recursion(k-1)

print(recursion(6))

'''
6
6 + 5 + 4 + 3 + 2 + 1
21
'''

