## Write a python function to remove a given word from a list-
## and strip it at the same time

def remove_Split(string,word):
    string = string.replace(word,"")
    print(string.strip())


sentence = "        Happy New Year buddy       "


remove_Split(sentence,"buddy")

# The strip() method removes any leading (spaces at the beginning)-
# and trailing (spaces at the end) characters (space is the default-
# leading character to remove)