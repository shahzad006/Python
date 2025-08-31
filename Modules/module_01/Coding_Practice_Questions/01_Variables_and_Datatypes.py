# ---------------------------------------------------------------------------- #
#                                   Questions                                  #
# ---------------------------------------------------------------------------- #

#* Q1: Create a variable for your name, age, and country. Print them.

name = "Muhammad Shahzad"
age = 22
country = "Pakistan"

print(name)
print(age)
print(country)


# ---------------------------------------------------------------------------- #

#* Q2: Swap two numbers using a temporary variable.

num1 = 5
num2 = 10

# Print original values
print("Before swapping:")
print("num1 =", num1)
print("num2 =", num2)

# Swap using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Print swapped values
print("After swapping:")
print("num1 =", num1)
print("num2 =", num2)



# ---------------------------------------------------------------------------- #


#* Q3: Swap without temporary variable


a, b = 5, 10
a, b = b, a
print(a, b)  # Output: 10 5


# ---------------------------------------------------------------------------- #

#* Q4: Input name & age


name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")


# ---------------------------------------------------------------------------- #


#* Q5: Convert string to int


num = "100"
result = int(num) + 50
print(result)  # Output: 150


# ---------------------------------------------------------------------------- #

#* Q6: Find the type of variables: 10, 10.5, "Hello", True.


name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
is_student = bool(input("Are you a student? : "))

print(type(name))
print(type(age))
print(type(is_student))


# ---------------------------------------------------------------------------- #

#* Q7: Take two floats from the user and print their sum.


num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

sum = num_1 + num_2

print(sum)


# ---------------------------------------------------------------------------- #


#* Q8: Area of circle

radius = float(input("Enter radius: "))
area = 3.14159 * radius * radius
print("Area =", area)


# ---------------------------------------------------------------------------- #

#* Q9: Celsius to Fahrenheit

celsius = float(input("Enter Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit =", fahrenheit)


# ---------------------------------------------------------------------------- #


#* Q10: Square & Cube

num = int(input("Enter a number: "))
print("Square:", num**2)
print("Cube:", num**3)

