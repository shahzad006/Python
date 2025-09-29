
# ---------------------------------------------------------------------------- #
#                              Exception Handling                              #
# ---------------------------------------------------------------------------- #


try:
    
    user_number_1 = int(input("Enter a number: "))
    user_number_2 = int(input("Enter another number: "))


    result = user_number_1 / user_number_2
    print("The result is:", result)

except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero is not allowed.")



# ---------------------------------------------------------------------------- #
#                              Multiple_Exceptions                             #
# ---------------------------------------------------------------------------- #

try:
    
    user_number_1 = int(input("Enter a number: "))
    user_number_2 = int(input("Enter another number: "))


    result = user_number_1 / user_number_2
    print("The result is:", result)

except ZeroDivisionError:
    # Code to handle the exception
    print("ZeroDivisionError: Division by zero is not allowed.")
except ValueError:
    print("ValueError: Invalid input. Please enter numeric values only.")

except SyntaxError:
    print("SyntaxError: There is a syntax error in the code.")


# ---------------------------------------------------------------------------- #
#                            Catching any Exception                            #
# ---------------------------------------------------------------------------- #


try:
    
    user_number_1 = int(input("Enter a number: "))
    user_number_2 = int(input("Enter another number: "))


    result = user_number_1 / user_number_2
    print("The result is:", result)
except Exception as e:
    # Code to handle the exception
    print("An error occurred:", str(e))


# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                                 Finally Block                                #
# ---------------------------------------------------------------------------- #

import time
time.sleep(1)
print("Starting the program...")
time.sleep(1)
print("Welcome to the calculator program!")



try:

    def table():
    

        user_inumber_1 = int(input("Enter a number: "))
        user_number_2 = int(input("Enter another number: "))
        opertation = input("Enter an operation (+, -, *, /): ")

        if opertation == '+':
            return user_inumber_1 + user_number_2
        elif opertation == '-':
            return user_inumber_1 - user_number_2
        elif opertation == '*':
            return user_inumber_1 * user_number_2
        elif opertation == '/':
            return user_inumber_1 / user_number_2
        else:
            return "Invalid operation. Please enter one of +, -, *, /."
        
    result = table()
    print("The result is:", result)

except Exception as e:
    # Code to handle the exception
    print("An error occurred:", str(e))

finally:
    print("Execution completed.")


# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                               Custom Exceptions                              #
# ---------------------------------------------------------------------------- #



user_input = input("Enter a positive number: ")
try:
    number = float(user_input)
    if number < 0:
        raise ValueError("The number must be positive.")
    print("You entered:", number)
except ValueError as ve:
    print("ValueError:", ve)