## program to create a dictionary of hindi words with values as their 
# english translation. provide user with an option to look it up.

myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are \n", myDict.keys())
a = input("Enter the Hindi word\n")
# print("The meaning of your word is:", myDict[a])
# The above line world throw an error if a key not present is called out for
print("The meaning of your word is:", myDict.get(a))


## program to input eight numbers from the user and display all the
# unique number(once)

num1 = int(input("Enter number 1:\n"))
num2 = int(input("Enter number 2:\n"))
num3 = int(input("Enter number 3:\n"))
num4 = int(input("Enter number 4:\n"))
num5 = int(input("Enter number 5:\n"))
num6 = int(input("Enter number 6:\n"))
num7 = int(input("Enter number 7:\n"))
num8 = int(input("Enter number 8:\n"))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)

## can we have set with 18(int, str, and float) as values in it?
s = {18, "18", 18.18}
print(s)

##what will be the length of the following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# ans : (2) - here 20 and 20.0 are counted the same so..




