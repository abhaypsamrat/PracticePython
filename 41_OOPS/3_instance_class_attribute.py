class Employee:
    company = "Microsoft"
    salary = 200

abhay = Employee()
ankit = Employee()

# Creating instace attribute salary for both the objects
abhay.salary = 700
ankit.salary = 500

print(abhay.company)
print(ankit.company)
print(abhay.salary)    # It print 700
print(ankit.salary)    # It print 500

