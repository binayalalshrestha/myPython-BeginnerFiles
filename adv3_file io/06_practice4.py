'''
A file contains a word "Donkey" multiple times.
You need to write a program which replaces this
world with ###### by updating the same file.
'''

with open('sample.txt','r') as f:
    content = f.read()

content = content.replace("donkey", "$%#@$%#")

with open('sample.txt', 'w') as f:
    f.write(content)