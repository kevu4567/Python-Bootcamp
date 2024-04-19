##numbers = [1, 2, 3, 4, 5]
##
##for num in numbers:
##    print(num)

"""
message = "Hello World!"

for char in message:
    print(char)

"""
"""
password = ""

while password != "correct":
    password = input("Enter the password: ")
print("Access granted!")



username = ""
password = ""

while (username != "infotek" or password != "infotek123"):
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    
print("Access granted!")


for i in range(1, 4, 1):
    for j in range(1, 4, 1):
        print(j, end = " ")
    print()
"""



#HW3
"""
# a) 1 3 5 7 9
for i in range(1, 10, 2):
    print(i, end = " ")

# b)  9 7 5 3 1
for i in range(9, 0, -2):
    print(i, end = " ")


# c) 1 8 27 64
for i in range(1, 5):
    print(i*i*i, end = " ")


# d) 64 27 8 1
for i in range(4, 0, -1):
    print(i*i*i, end = " ")


# e) triangle 
for i in range(1, 5, 1):
    for j in range(1, i+1, 1):
        print("*", end = " ")
    print()

#  0 to 3 triangle
for i in range(0, 4, 1):
    for j in range(0, i+1, 1):
        print(j, end = " ")
    print()

# invert triangle
for i in range(6, 1, -1):
    for j in range(1, i+1, 1):
        print("*", end = " ")
    print()
"""
#  0 to 3 invert triangle
for i in range(5, 0, -1):
    for j in range(0, i+1, 1):
        print(j, end = " ")
    print()




