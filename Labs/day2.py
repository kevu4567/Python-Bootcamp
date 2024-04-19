#for i in range (1, 101):
 #   print(i)

#for x in range (6):
#   print(x)
#else:
#    print("Finaly Finished")

##x = -2
##if x < 0:
##    print(x, "is negative")
##elif x == 0:
##    print(x, "is zero")
##else:
##    print (x, "is positive")
##
##



##grade = int(input("Enter your grade: "))
##
##if grade >= 90:
##   print(grade, "is a A grade")
##elif grade >= 80:
##    print(grade, "is a B grade")
##elif grade >= 70:
##    print(grade, "is a C grade")
##else:
##    print (grade, "is a D grade")
##



##age = int(input("Enter the age: "))
##
##if (age >= 25 and age <= 44):
##   print("You are allowed to rent a car")
##elif age < 25:
##    print("You are not allowed to rent a car")
##elif age >= 45:
##    print("You get a special discount: 10%")


'''
## Positive vs Negative:  HW
#number = int(input("Enter the Number: "))

#if number > 0:
#   print("Positive Number")
#else:
#   print("Negative Number")
'''


## Compare two number
##    
##number1 = int(input("Enter the Number1: "))
##number2 = int(input("Enter the Number2: "))
##print("Maximum Number is ", max(number1, number2))




## Ask user to enter the years of service and current salary, add the following logic

## if employee years of service is 5 or more AND salary is greater than 5,000 

##          then they get additional 2,000 bonus otherwise they get 1,000 bonus
##
##years = int(input("Enter the years of service: "))
##salary = int(input("Enter the current salary: "))
##
##if years >= 5 and salary > 5000:
##   print("Total salary", salary + 2000)
##else:
##   print("Total salary", salary + 1000)



## 2) As we explained login program ask user to enter username, password and pin ,
##        if all is correctly enter then show login successful otherwsie show login fail
username = "kevu4567"
password = "infotek123"
pin = 321

userinput = input('Enter your username: ')
userpass = input('Enter your password: ')
userpin = int(input('Enter your pin: '))

if userinput == username and userpass == password and userpin == pin:
    print("Login successful")
elif userinput != username and userpass == password and userpin == pin:
    print("Login fail! You enter wrong username")
elif userinput == username and userpass != password and userpin == pin:
   print("Login fail! You enter wrong password")
elif userinput == username and userpass == password and userpin != pin:
   print("Login fail! You enter wrong pin")
elif userinput != username and userpass != password and userpin != pin:
    print("Login fail! You enter wrong username, password and pin")

#-----------------------------------------------------------------------------

#3
name = input('Please enter your name: ')
sub1 = int(input('Please enter your score for subjet 1: '))
sub2 = int(input('Please enter your score for subjet 2: '))
sub3 = int(input('Please enter your score for subjet 3: '))
total = sub1 + sub2 + sub3
avg = total / 3
grade = ""
passorfail = ""

if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

if avg >= 60:
    passorfail = "You Pass"
else:
    passorfail = "you Fail"

print("Hello " + name)
print("Subject 1 score " + str(sub1))
print("Subject 2 score " + str(sub2))
print("Subject 3 score " + str(sub3))
print("Your total score is " + str(total))
print("your average score is " + str(round(avg, 2)) + "%")
print("Your grade is " + grade)
print(passorfail)

#-----------------------------------------------------------------------------

#4
length = int(input('What is the length of the rectangle: '))
width = int(input('What is the width of the rectangle: '))

area = length * width

print("Your rectangle's area is " + str(area))



