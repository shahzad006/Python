# ---------------------------------------------------------------------------- #
#                                  Collections                                 #
# ---------------------------------------------------------------------------- #

#* Q1: Create a list of 5 animals. Print the first and last.


animals = ["Cat", "Dog", "Lion", "Tiger", "Cow"]

print("First animal:", animals[0])
print("Last animal:", animals[-1])




# ---------------------------------------------------------------------------- #


#* Q2: Add new item to list

animals = ["Cat", "Dog", "Lion", "Tiger", "Cow"]
animals.append("Elephant")
print(animals)

# ---------------------------------------------------------------------------- #

#* Q3: Remove item from list

animals = ["Cat", "Dog", "Lion", "Tiger", "Cow"]
animals.remove("Cat")
print(animals)



# ---------------------------------------------------------------------------- #

# Q24: Tuple example

numbers = (10, 20, 30, 40)
print(numbers)


# ---------------------------------------------------------------------------- #


#* Q5: Set example

my_set = {1, 2, 3, 4, 5}
print(my_set)


# ---------------------------------------------------------------------------- #

#* Q6: Dictionary example

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)



# ---------------------------------------------------------------------------- #

# Q6: Check number in set

my_set = {1, 2, 3, 4, 5}

num = 3
if num in my_set:
    print(num, "is in the set")
else:
    print(num, "is not in the set")






# ---------------------------------------------------------------------------- #

#* Q7: Dictionary of countries

countries = {
    "Pakistan": "Islamabad",
    "India": "New Delhi",
    "China": "Beijing"
}
print("Capital of Pakistan:", countries["Pakistan"])


# ---------------------------------------------------------------------------- #

#* Q8: Add new key-value pair


countries = {
    "Pakistan": "Islamabad",
    "India": "New Delhi",
    "China": "Beijing"
}


countries["USA"] = "Washington DC"
print(countries)

# ---------------------------------------------------------------------------- #


#* Q9: Loop through dictionary keys


countries = {
    "Pakistan": "Islamabad",
    "India": "New Delhi",
    "China": "Beijing"
}


for country in countries.keys():
    print("Country:", country)



# ---------------------------------------------------------------------------- #



#* Q10: Loop through dictionary values

countries = {
    "Pakistan": "Islamabad",
    "India": "New Delhi",
    "China": "Beijing"
}

for capital in countries.values():
    print("Capital:", capital)

