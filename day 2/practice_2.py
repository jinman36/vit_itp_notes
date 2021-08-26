# This is a number magic trick
# Pick a number from 1 - 9
# Multiple by 2
# Add 10 to the total
# Divide by 2
# Subtract by the original number

# Final number is 5



# Take an user's input
# Assign a new variable for each step
# at the end, use an if statement to see if the final is always 5!


# validation_rule = type(int(21))

user_guess= int(input("Guess a number between 1 and 9: "))
user_guess_mult = user_guess*2
user_guess_add = user_guess_mult + 10
user_guess_div = user_guess_add/2
user_guess_final = int(user_guess_div) - user_guess

if user_guess_final == 5:
  print('Your guess will always be = ', + user_guess_final)
else:
  print('you cheated')




