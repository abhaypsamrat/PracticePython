class Employee:
    company = "Google"
    salary = 5500
    bonussalay = 500
    # totalSalary = 6000
     
    @property
    def totalSalary(self):
        return self.salary + self.bonussalay

e = Employee()
print(e.totalSalary)
