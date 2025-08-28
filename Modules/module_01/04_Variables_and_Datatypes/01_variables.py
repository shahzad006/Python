
#? ----------------------------------1: String ---------------------------------- #

name_1 = 'Muhammad'
name_2 = "Shahzad"
name_3 = """Muhammad Shahzad"""
print(name_1 , type(name_1))
print(name_2 , type(name_2))
print(name_3 , type(name_3))


#todo  Concatenation
full_name = name_1 + " " + name_2
print(full_name, type(full_name))  


#todo Reapeating Strings
repeated_name = name_1 * 3
print(repeated_name, type(repeated_name))

#todo Indexing and Slicing
first_char = name_1[0]  
print(first_char, type(first_char))  

sliced_name = name_1[0:4]
print(sliced_name, type(sliced_name)) 

#todo F strings
greeting = f"Hello, {name_1} {name_2}!"
print(greeting, type(greeting))




#? ----------------------------------2: Integer --------------------------------- #
age_1 = 25
age_2 = 30
print(age_1 , type(age_1))
print(age_2 , type(age_2))




#? ----------------------------------3: Float ----------------------------------- #
price_1 = 99.99
price_2 = -49.99
print(price_1 , type(price_1))
print(price_2 , type(price_2))



#? ----------------------------------4: Boolean -------------------------------- #
is_active_1 = True
is_active_2 = False
print(is_active_1 , type(is_active_1))
print(is_active_2 , type(is_active_2))



#? ----------------------------------- None ----------------------------------- #

is_available = None
print(is_available, type(is_available))



#? ----------------------- Case-Sensitivity in Variable Names ------------------ #

# Variable names are case-sensitive
userName = "Alice"
user_name = "Bob"
print(userName)  # Output: Alice
print(user_name)  # Output: Bob



#? --------------------------- Invalid variable Name -------------------------- #

# Invalid variable names (uncommenting these will raise errors)

#! 1user = "Ali"  # Invalid - cannot start with a number
#! print = 10      # Invalid - cannot use reserved words

