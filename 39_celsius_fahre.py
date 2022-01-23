# convert celsius to fahrenheit

def farh(cel):
    return (cel * (9/5)) + 32

c = 37
f = farh(c)
print('fahreheit tempreture is ' + str(f))