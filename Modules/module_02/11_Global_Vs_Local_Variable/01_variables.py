# ---------------------------------------------------------------------------- #
#?                          Global Vs Local Variable                           #
# ---------------------------------------------------------------------------- #


# ------------------------------ Global Variable ----------------------------- #

# x = 10

# def number():
#     print(x) # Accessing global variable inside function

# number()

# ---------------------------------------------------------------------------- #

# ------------------------------ Local Variable ------------------------------ #


# def sum():
#     number_1 = 3
#     number_2 = 7
#     print(number_1 + number_2) # Accessing local variable inside function

# sum()
# print(number_1) # Accessing local variable outside function (will raise an error)
# print(number_2) # Accessing local variable outside function (will raise an error)


# ---------------------------------------------------------------------------- #


# ----------------------------- Local and Global ----------------------------- #

# global_var = "Global Variable"

# def my_function():
#     local_var = "Local Variable"
#     print(global_var)  # Accessing global variable inside function
#     print(local_var)   # Accessing local variable inside function


# my_function()
# print(global_var)  # Accessing global variable outside function
# print(local_var)   # Accessing local variable outside function (will raise an error) 


# ---------------------------------------------------------------------------- #

# ---------------------------- Enclosing variables --------------------------- #


# num_1= 4 # Global variable
# print(f"Global variable: {num_1}")

# def sum():
#     num_2 = 6 # enclosing variable
#     print(f"Enclosing variable: {num_2}")

#     def add():
#         num_3 = 8 # local variable
#         print(f"Local variable: {num_3}")
#         print(num_1 + num_2 + num_3) # Accessing all variables inside nested function



#     add()

# sum()

# print(f"Global variable : {num_1}")
# print(f"Enclosing variable : {num_2}") # Accessing enclosing variable outside function (will raise an error)
# print(f"Local variable : {num_3}") # Accessing local variable outside function (will raise an error)


# ---------------------------------------------------------------------------- #


