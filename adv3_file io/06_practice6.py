## Write a program to mine a log file and find out whether it contains "python"

with open("log.txt") as f:
    content = f.read().lower()

if 'python' in content:
    print("Yes python is present")
else:
    print("python not present")