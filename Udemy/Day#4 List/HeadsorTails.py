# import random

# random_integer = random.randint(1, 10)  #  Generates a random integer between 1 and 10 both including
# print(random_integer)

# random_float = random.random()  # Generates a number between 0.00000000 to 0.9999999... but not including 1.0
# print(random_float)
# print(random_float * 5)  # Generates a number between 0.0000000 to 4.99999999


#  To toss a coin virtually, we can also make the game of Heads and Tails using randomization
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random	 
#Write the rest of your code below this line 👇

a = ['Heads', 'Tails']        #  Using the python list

print(random.choice(a))
