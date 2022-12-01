# Adding values to an empty set
b = set()
b.add(4)
b.add(5)
b.add(5) #adding a value repeatedly does not change a set
b.add((4, 5, 6))
print(b)
#cannot add list or dictionary to a set as values of lists can be chnaged
#can add tuple though because tuples cannot be changed

print(len(b)) #prints the length of the set

b.remove(5) #removes 5 from set
print(b)

print(b.pop())
print(b)