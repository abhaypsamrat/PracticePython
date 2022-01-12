l1 = [4, 14, 2, 31, 10, 5]

l1.sort()   #sort the list
print(l1)    

l1.reverse()    # reverse the list
print(l1)    

l1.append(20)  # add 20 at the end of list
print(l1)     

l1.insert(1, 100)  # insert 100 at the index of 1
print(l1)          # it return --> [31, 100, 14, 10, 5, 4, 2, 20]

l1.pop(2)    # remove element at index 2
print(l1)

l1.remove(31)  # remove 31 from the list
print(l1)