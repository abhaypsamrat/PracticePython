class Employee:
    company= "Amazon"
    salary= 1000
    location= "Delhi"

    # def changeSalary(self, sal):
    #     self.salary = sal
  
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)             # It print -> 1000
e.changeSalary(4000)        
print(e.salary)             # It print -> 4000
print(Employee.salary)      # It print -> 4000