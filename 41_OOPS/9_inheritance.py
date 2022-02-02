class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an Employee")

class Programmmer(Employee):  #Programmer class inherite from Employee class
    language = "Python"

    def getLanguage(self):
        print(f'the language is {self.language}')

e = Employee()
e.showDetails()

p = Programmmer()
p.getLanguage()