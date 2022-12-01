greeting = "Good Morning, "
name = "Binaya"
'''
[ B   i   n   a   y   a]
[ 0   1   2   3   4   5]
[-6  -5  -4  -3  -2  -1]
'''
greet = greeting + name #concatenating two strings
print(greet)

print(name[0:3])#python only counts till index 2 in condition

print(name[:6])#is same as name[0:6]
print(name[1:])#is same as name[1:6]

print(name[-4:-1])#is same as name[2:5]


name2 = "Tommy Cruise"
'''
T o m m y   C r u i s  e
0 1 2 3 4 5 6 7 8 9 10 11
'''
d = name2[0:12:3] #[startIndex:endIndex:skipValue]
print(d)
