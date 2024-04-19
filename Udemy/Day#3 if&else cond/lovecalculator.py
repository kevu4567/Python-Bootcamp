# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Calculation
combined_string = name1 + name2
lower_name = combined_string.lower()

count_t = lower_name.count("t");
count_r = lower_name.count("r");
count_u = lower_name.count("u");
count_e = lower_name.count("e");

count_l = lower_name.count("l");
count_o = lower_name.count("o");
count_v = lower_name.count("v");
count_e = lower_name.count("e");

x = count_t + count_r + count_u + count_e
y = count_l + count_o + count_v + count_e
string_true = str(x)
string_love = str(y)
percentage = int(string_true + string_love)

# For output
if (percentage < 10) or (percentage > 90):
    print(f"Your score is {percentage}, you go together like coke and mentos.")
elif(percentage >= 40) and (percentage <= 50):
    print(f"Your score is {percentage}, you are alright together.")
else:
    print(f"Your score is {percentage}.")

