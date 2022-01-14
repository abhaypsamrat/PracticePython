# This syntax is empty Dictionary not set
a = {}
print(type(a))

# This syntax is empty set
b = set() 
print(type(b))

# Adding value in empty set
# set con not print repeated elements
b.add(10)
b.add(10)
b.add(4)
b.add(5)
b.add(5)
print(b)    # return only --> {10, 5}

# Print len of set
print(len(b))

# remove elements in set
b.remove(5)  # remove 5 in set
print(b)