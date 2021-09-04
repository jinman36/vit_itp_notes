# reference https://datagy.io/python-f-strings/
# f_strings are more like object literals with concatenations

name = 'Jeff'

# Hi! my name is Jeff

# print("Hi! my name is %s" %(name))
print(f'Hi! My name is {name}')

# Will also allow evaluating expressions
print(f"2 + 3 is equal to {2+3}")

# using variables
height = 2
base = 3

print(f'area of triangle is equal to {base*height/2}')

# dictionaries
# person = {
#   'name': 'Jeff',
#   'age': 38,
#   'gender': 'male'
# }
# print(f"{person.get('name')} is {person.get('age')} years old.")

# people = [{
#   'name': 'Jeff',
#   'age': 38,
#   'gender': 'male'
# },
# {
#   'name': 'Sandra',
#   'age': 36,
#   'gender': 'Female'
# }
# ]

  # print(f"{person.get('name')} is {person.get('age')} years old.")

# person = {
#   'gender': 'male',
#   'name': 'Mary"'
# }

# for person in people:
#   print(f"{'She' if person.get('gender') == 'female' else 'He'} went to the store.")

# left align text
# print(f'{"apple" : >30}')
# # right align
# print(f'{"banana" : <30}')
# # center align
# print(f'{"Orange" : ^30}')

# number = 0.9124325345
# large_number = 126783.6457

# # with 2 decimal points
# print(f"{number:.0%}")
# # with no decimal points
# print(f"{number:.0%}")
# #  with 3 precision factors
# print(f"{number:.3f}")

# # value as cash
# print(f"${large_number:.2f}")
# # value comma seperated
# print(f"${large_number:,.2f}")
# # value with exponents
# print(f"{large_number:e}")

#  new feature to print to console with repeating code
number = 2
print(f"{number = }")


