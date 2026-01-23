student_heights = input("Input a list of student heights:\n ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
number = 0

for student_height in student_heights:
    total_height += student_height
    number += 1

average = total_height/ number

print(f"The sum of their heights is {total_height}.")
print(f"The average is {average}.")