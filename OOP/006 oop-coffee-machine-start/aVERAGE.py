student_height = [180, 124, 165,  173, 189, 169, 146]

numb = 0
total = 0

for i in student_height:
    total += i
    numb += 1
average = total / numb
print(round(average))
