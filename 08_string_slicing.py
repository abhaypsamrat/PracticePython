greeting = 'Good Morning, '
name = 'Abhay'

# Concenating two string
print(greeting + name)
# add = greeting + name
# print(add)

#Access the specific character of string
print(greeting[0])
print(name[3])

# slicing the string
print(name[0:3])  # return 'Abh' --> charaters from 0,1 & 2
print(name[1:4])  # return 'bha' --> charaters from 1,2 & 3

print(name[-1])   # It print value from last index

print(name[-4:-1])  # return --> 'bha'

name='HiThisIsAbhay'
print(name[0:12:2])  # It return --> "HtiTAh" print a value & skip 2 value from 0 to 12