def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3] + marks[4])/500)*100
    return p

marks1 = [70, 71, 72, 73, 74]
percentage1 = percent(marks1)

marks2 = [60, 61, 62, 63, 64]
percentage2 = percent(marks2) 

print(percentage1, percentage2)