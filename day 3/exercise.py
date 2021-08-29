# ITP Week 1 Day 3 Exercise

# EASY


# print(uppercase)
# 1. loop through the lowercase and print each element

# 2. loop through the lowercase and print the capitalization of each element

# MEDIUM

# 1. create a new variable called uppercase with an empty list

# 2. loop through the lowercase list
    # 2a. append the capitalization of each element to the uppercase list
# HARD

# A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.
# 1. create the following variables and assign them Booleans as False

# 2. loop through the string password (same as a list)
# OR you can create a new list variable of the string password
# using list(string) NOTE: assign it a new variable as such:
# password_list = list(password) prior to looping.

# Password - User input for flex goal
# password = "MySuperSafePassword!@34"
password = input("Please check if your password is valid: ")

# Manual check lists
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = []
number_list = []
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# loops to populate manual lists
for letter in lowercase:
  uppercase.append(letter.capitalize())

number_range = range(0, 10)
for num in number_range:
  number_list.append(str(num))

# Validation booleans
has_uppercase = False
has_lowercase = False
has_special_char = False
has_number = False

# logic for password checking
if any(element1 in uppercase for element1 in password):
    has_uppercase = True
if any(element2 in lowercase for element2 in password):
    has_lowercase = True
if any(element3 in special_char for element3 in password):
    has_special_char = True
if any(element4 in number_list for element4 in password):
    has_number = True


# validation readout for output - Nightmare Flex Goal
if has_uppercase != True:
  print("Pasword Requires 1 Upper Case letter")
elif has_lowercase != True:
  print("Pasword Requires 1 Lower Case letter")
elif has_special_char != True:
  print("Pasword Requires 1 Special character")
elif has_number != True:
  print("Pasword Requires 1 Number")
else:
  print("Password is valid")

# Original proof of life logic
# print(has_uppercase)
# print(has_lowercase)
# print(has_special_char)
# print(has_number)



# 3. For each iteration of the loop, create a if statement
# check to see if it exists in any of the list by using IN
# if it does exist, update the appropriate variable and CONTINUE
# not break.

# NOTE: to see if it has a number, use range from 0 - 10!

# 4. do a final check to see if all of your variables are TRUE
# by using the AND operator for all 4 conditions. (This is done for you, uncomment below)

# final_result = has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True

# NOTE: we can shorthand this by just checking if the variable exists (returns True)
#final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
# this will fail the same if any one of them is False

# If the final_result is true, print "SAFE STRONG PASSWORD"
# else, print "Update password: too weak"
# NOTE: this must be done outside of the loop

# BONUS: update the password variable to take in an user input!

# NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!

