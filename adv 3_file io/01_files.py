# use open function to read the content of a file
f = open('sample.txt', 'r')
# by default the mode is r
# w - writing, a - append, + - updating
# 'rb' will open for read in binary mode
# 'rt' will open for read in text mode
data = f.read()
print(data)
f.close()

f = open('sample.txt', 'r')
data = f.read(5) # reads first 13 characters from the file
print(data)
f.close()
