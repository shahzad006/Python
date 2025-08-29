# ---------------------------------------------------------------------- #
#                          Conditional_Statements                        #
# ---------------------------------------------------------------------- #

#* Write a program to check if a number is even or odd.

user_input = int(input("Enter a number: "))

if user_input % 2 == 0:
    print(f"{user_input} is an even number.")
else:
    print(f"{user_input} is an odd number.")



# ---------------------------------------------------------------------------- #
#* Check which number is greater among two numbers.


number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))


if number_1 > number_2:
    print(f"{number_1} is greater {number_2}")
else:
    print(f"{number_2} is greater {number_1}")




# ---------------------------------------------------------------------------- #

#* Check if a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print(f"Positive : {num}")
elif num < 0:
    print(f"Negative : {num}")
else:
    print(f"Zero : {num}")



# ---------------------------------------------------------------------------- #

#* Write a program to check if a person is eligible to vote (age ≥ 18).

user_input = int(input("Enter a number: "))

if user_input > 18:
    print("You are eligible for VOTE")
else:
    print("You are not eligible for VOTE")



# ---------------------------------------------------------------------------- #

#* Write a program to calculate the grade based on marks obtained in three subjects.

english = int(input("Enter your English marks 1 to 100 :"))
urdu = int(input("Enter your Urdu marks 1 to 100 :"))
math = int(input("Enter your Math marks 1 to 100 :"))
sum = english + urdu + math
print(f"Total Marks : {sum}")


if sum >= 270:
    print("Grade A+")
elif sum >= 250 and sum < 270:
    print("Grade A")
elif sum >= 230 and sum < 250:
    print("Grade B")
elif sum >= 200 and sum < 230:
    print("Grade C")
else:
    print("Fail")



# ---------------------------------------------------------------------------- #

#* Check if a given year is a leap year.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
