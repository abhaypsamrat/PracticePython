# Check your grade by giving input marks

mark = int(input('Enter your marks: '))

if mark>=90:
    grade = 'Ex'
elif mark>=80:
    grade = 'A'
elif mark>=70:
    grade = 'B'
elif mark>=60:
    grade = 'C'
elif mark>=50:
    grade = 'D'
else:
    grade = 'F'

print("Your Grade is: " + grade)