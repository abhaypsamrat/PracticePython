# Find the maximum of given 3 value

def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    elif(num2>num3):
        return num2
    else:
        return num3

m = maximum(44, 23, 6)
print("maximum is " + str(m))