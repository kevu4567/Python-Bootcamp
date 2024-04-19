#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easypassword = ""
hardpassword = ""

add_symbols = ""
add_numbers = ""
add_letters = ""

for char in range(1, nr_letters + 1):
    add_letters += random.choice(letters)
for char in range(1, nr_symbols + 1):
    add_symbols += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    add_numbers += random.choice(numbers)   
    # string concatenation
easypassword = add_letters + add_symbols + add_numbers
print(f"Easy Password: {easypassword}") #print(easypassword)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for char in range(1, nr_letters + 1):
    hardpassword += random.choice(letters)
    hardpassword += random.choice(symbols)
    hardpassword += random.choice(numbers)
print(f"Hard Password: {hardpassword}") #print(hardpassword)  