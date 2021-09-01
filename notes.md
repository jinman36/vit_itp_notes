## Data structures - dictionaries

Links
https://www.w3schools.com/python/python_ref_keywords.asp
https://www.w3schools.com/python/python_ref_functions.asp
https://www.w3schools.com/python/python_ref_string.asp
https://www.w3schools.com/python/python_ref_list.asp
https://www.w3schools.com/python/python_ref_dictionary.asp

-------------
- control + D will select all matching words in the folder

- Still in the basics but doing things that will get into the complicated parts

- Lists and Dictionaries

- Dictionaries are groups that are key value pairs - example below

<!-- my_car {
  "brand": "ford",
  "model": "Mustang",
  "year", 2021,
} -->

- dictionaries after python version 3.7 are ordered
- in python 3.6 and earlier, dictionaries are unordered

- Additional code that we played with in class
-----------------------------------------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
y = car.values()
z = car.items()


car["condition"] = "fair" # new key created
car["year"] = 2018

print(x)
print(y)
print(z)

if "Mustang" in car.values():
  print("Yes, 'model' is one of the keys in the car dictionary")
---------------------------------------
- Update will assign a value if the item dosent exist
car.update({"year": 2020})


