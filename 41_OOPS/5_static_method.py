class Employee:
    company = 'TCS'
    salary = '25k'
    post = 'beginner'
    def getSalary(self):
        print('salary is 25k')

    @staticmethod
    def greet():
        print('Good Morning')

abhay = Employee()
abhay.getSalary()
abhay.greet()