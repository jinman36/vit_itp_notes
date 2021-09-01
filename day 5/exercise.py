# ITP Week 2 Day 1 Exercise


# Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 1
}

# SCENARIO: A person came in and bought one of everything!

for item in inventory:
    inventory[item] -= 12
    
    # decrement item by using an assignment operator (Day 2 Lecture line #130)

    # NOTE: recall that item represents the key of the key:value pair

# SCENARIO: REMOVE ANY 0 ITEMS

for item in list(inventory):
    if inventory[item] < 1:
        inventory.pop(item)
    # use an if statement to check if the value is 0 and then remove it

print(inventory)