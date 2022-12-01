## Create an empty dictionary. Allow 4 friends to enter their facoutire language as values and
# use keys as their names. Assume that the names are unique.

favLang = {}
a = input("Enter your favorite language shubham\n")
b = input("Enter your favorite language ankit\n")
c = input("Enter your favorite language sonali\n")
d = input("Enter your favorite language harshita\n")
favLang['shubham'] = a
favLang['ankit'] = b
favLang['sonali'] = c
favLang['harshita'] = d

print(favLang)

#keys cannot be same but values can be same, when keys are same- it updates the value

##can you cahnge the values inside a list which is contained in set s
## s = { 8, 7, 12, "Harry", [1, 2]}
## Ans : First thing, u cannot add a list to a set as objects in a set cannot be changed and lists can be cahnged