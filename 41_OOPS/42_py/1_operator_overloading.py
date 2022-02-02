class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("lets add")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("lets multiply")
        return self.num * num2.num

n1 = Number(10)
n2 = Number(20)
sum = n1 + n2      # It print -> lets add
mul = n1 * n2      # It print -> lets multiply
print(sum)         # It print -> 30
print(mul)         # It print -> 200