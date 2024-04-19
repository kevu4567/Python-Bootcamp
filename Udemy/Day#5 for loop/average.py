# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0   # Counter Method
for  height in student_heights:
  total_height += height
print(f"total height = {total_height}")

# This loop essentially counts the number of items in the student_heights list, 
# providing the count of students.
number_of_student = 0    # By Naive approach (_)
for _ in student_heights:
  number_of_student += 1
print(f"number of students = {number_of_student}")

# This replicate the len function of python
number_count = 0
for number in student_heights:
  number_count += 1
print("number of students =", number_count)


average_height = total_height / number_of_student
print("average height =", round(average_height))