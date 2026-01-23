student_scores = input("Input a list of student scores:\n ").split() 10]
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

score = 0
for student_score in student_scores:
    if student_score > score:
        score = student_score
print(score)
    