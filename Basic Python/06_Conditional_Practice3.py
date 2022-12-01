# A spam comment is defined as a text containing following keywords:
# "make a lot of money", "buy now", "subscribe this"
# "click this". Write a program to detect these spams.

text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")

print("\n")


# Write a program to find whethet a given username contains less than 10 characters or not.
username = input("Enter Username: \n")
print(len(username))
if (len(username) < 10):
    print("Username contains less than 10 characters")
else:
    print("Username contains more than 10 characters")

print("\n")


# Write a program which finds out whether a given name is present in a list or not.
names = ["harry", "shubham", "rohit", "rohan", "aditi", "shipra"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")

print("\n")