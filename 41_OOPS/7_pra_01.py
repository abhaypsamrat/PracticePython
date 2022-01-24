class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and working in {self.product}")

abhay = Programmer("Abhay", "Windows 13")
ankit = Programmer("Bill Gates", "Github")
abhay.getInfo()
ankit.getInfo()