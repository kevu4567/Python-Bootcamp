target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

even_sum = 0
# Write your code here 👇
# This will addd even numbers from 0 to target
for number in range(target+1): # Add +1 to include target
  if number % 2 == 0:
    even_sum += number

print(even_sum)
