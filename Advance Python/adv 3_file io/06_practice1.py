# Write a program to read the text from a given file 'poems.txt' and
# find out whether it contains the word 'twinkel'

f = open('poems.txt','r')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present\n")
else:
    print("Twinkle is not present\n")
print (t)
f.close()