# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
max_value = 0
for index in range(0, len(student_scores)):
    if index == 0:
        max_value = student_scores[index]
    elif student_scores[index] > max_value:
        max_value = student_scores[index]

print(f'The highest score in the class is: {max_value}')
