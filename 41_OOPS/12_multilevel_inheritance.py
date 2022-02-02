class Person:
    city = "Varanasi"

    def status(self):
        print("I am Student")

class Employee(Person):
    company = "Tata"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def status(self):
        print("I am Employee")

class Programmer(Employee):
    company = "Fiver"

    def getSalary(self):
        print(f"No salary to programmer")

p = Person()
p.status()         # It print -> I am Student
e = Employee()
e.status()         # It print -> I am Employee
pr = Programmer()
pr.status()       # It also print -> I am Employee