students_heights = input("Input a list of student heights ").split()
for n in range(0, len(students_heights)):
  students_heights[n] = int(students_heights[n])
print(students_heights)

total_height = 0

for height in students_heights:
  total_height += height

number_of_students = 0

for number in students_heights:
  number_of_students += 1

average_heights = round(total_height / number_of_students)
print(average_heights)