## Write a program to find out whether a file is identical and matches
## the content of another file.

file1 = "copy.txt"
file2 = "this.txt"

with open("copy.txt","r") as f:
    content = f.read()

with open("this.txt") as f:
    content2 = f.read()

    if content == content2:
        print("identical")
    else:
        print("non-identical")