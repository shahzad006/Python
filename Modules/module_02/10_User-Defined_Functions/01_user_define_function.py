# ---------------------------------------------------------------------------- #
#?                             User-Defined_Functions                          #
# ---------------------------------------------------------------------------- #




def name():
    print("Muhammad Shahzad")

name()

# ---------------------------------------------------------------------------- #

def name():
    return "Muhammad Shahzad"

name_1 = name()
print(name_1)


# ---------------------------------------------------------------------------- #

def greeting():
    return "Hello, welcome to Python programming!"

greeting_1 = greeting()
print(greeting_1)



# ---------------------------------------------------------------------------- #

def add_numbers(num1, num2):
    return num1 + num2

add_numbers_1 = add_numbers(5, 10)
print(add_numbers_1)

# ---------------------------------------------------------------------------- #


def name(a="Muhammad Shahzad"):
    return a

name_1 = name()
print(name_1)


# ---------------------------------------------------------------------------- #


def greet(first_name, last_name):
    print("Hello", first_name, last_name)

greet(first_name="Muhammad", last_name="Shahzad")



# ---------------------------------------------------------------------------- #

def greeting(*names):
    for i in names:
        print("Hello", i)
    
    return names

names_1 = greeting("Muhammad", "Shahzad", "Ali", "Ahmed")
print(names_1)
