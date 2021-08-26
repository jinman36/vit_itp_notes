# ITP Week 1 Day 2 Exercise

# Take an user's input for his age
user_age = input("What is your age? ")
validation_rule = type(int())
# The user input comes in as a string so we have to cast it to a int!
# user_age_int = int(user_age)
# Use an if/else to determine if they are of legal drinking age.
# if the user is of age, print "Welcome!"
# else, tell them to come back in X amount of years (use math operations)
if type(user_age) != validation_rule:
  print('What did you enter?')
elif user_age >= 21:
  print("Welcome!")
else:
  print('come back in', (21 - user_age), 'years!')


# Bonus: Add a validation by checking the type of the user input
# to ensure it can be casted as an int. Handle any other input that
# are not numbers to try again.
