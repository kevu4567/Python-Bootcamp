'''
def greet():
    print ("Hello World")

# Call the function
greet()

print ('Outside Function')


def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print ('Square:',  square)


## HomeWork   07/20/23


# - Write a function to create function to calculate mpg(miles, gallons)
miles = float(input("Enter the number of miles:"))
gall = float(input("Enter the number of gallons:"))

def find_mpg(miles, gall):
    result = miles / gall
    return result

# function call
mpg = find_mpg(miles, gall)

print ('Calculated mpg:', mpg, 'mpg')



def find_sum(num1, num2, num3):
    result = num1 + num2 + num3
    return result

# function call
add = find_sum(5, 6, 10)

print ('The sum of three numbers is:',  add)

# - Write a function to create function to calculate Salary (hr, rate)
hr = int(input("How many hrs you worked:"))
rate = int(input("Enter the rate per hour:"))

def find_salary(hr, rate):
    result = hr * rate
    return result

# function call
salary = find_salary(hr, rate)

print ('The total salary you will receive: $',  salary)

#  Write a function to find max(20,30)
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

def max_num(num1, num2):
    result = max(num1, num2)
    return result

# function call
maximum = max_num(num1, num2)

print ('Max num between two is:',  maximum)


# - Write a function to find min(20,30)
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

def min_num(num1, num2):
    result = min(num1, num2)
    return result

# function call
minimum = min_num(num1, num2)

print ('Min num between two is:',  minimum)



# Find the area of rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Ask the user for the input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_rectangle_area(length, width)
print("The area of the rectangle is:", area)

'''
# Find the area of triangle
def calculate_triangle_area(base, height):
    return (1/2) * base * height

# Ask the user for the input
base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of the triangle: "))

# Function call
area = calculate_triangle_area(base, height)

print("The area of the triangle is:", area)



#  Write a function to calculate a Grade Character,   findGrade(s1,s2,s3)
# if average of three subjects is less than 60 then display grade: F




