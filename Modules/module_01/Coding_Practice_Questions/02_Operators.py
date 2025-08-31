# ---------------------------------------------------------------------------- #
#                                   Operators                                  #
# ---------------------------------------------------------------------------- #


#* Q1: Find remainder

num = int(input("Enter a number: "))
print("Remainder when divided by 2:", num % 2)


# ---------------------------------------------------------------------------- #

#* Q2: Check equality

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == b:
    print("Both are equal")
else:
    print("Not equal")


# ---------------------------------------------------------------------------- #

#* Q3: Simple Interest

P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))
SI = (P * R * T) / 100
print("Simple Interest =", SI)



# ---------------------------------------------------------------------------- #

#* Q4: Find the average of 5 numbers.


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
num5 = float(input("Enter fifth number: "))

average = (num1 + num2 + num3 + num4 + num5) / 5
print("Average =", average)


# ---------------------------------------------------------------------------- #

#* Q5: Take two numbers and print the maximum using conditional operator.

num_1 = int(input("Enter a number :"))
num_2 = int(input("Enter second number :"))

if num_1 >= num_2:
    print(f"{num_1} is maximum")
else:
    print(f"{num_2} is maximum")

# ---------------------------------------------------------------------------- #

#* Q6: BMI Calculator


wight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = wight / (height ** 2)

print(bmi)




# ---------------------------------------------------------------------------- #

#* Q7: Divisible by 2 and 3

num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by 2 and 3")
else:
    print("Not divisible by 2 and 3")


# ---------------------------------------------------------------------------- #

#* Q8: Power of a number

x = int(input("Enter base: "))
y = int(input("Enter exponent: "))
print("Result =", x ** y)



# ---------------------------------------------------------------------------- #

#* Q9: Age check with and/or

age = int(input("Enter your age: "))
if age >= 18 and age <= 60:
    print("You are in working age")
else:
    print("You are not in working age")


# ---------------------------------------------------------------------------- #

#* Q10: Positive, Negative, or Zero

num = int(input("Enter a number : "))

if num > 0 :
    print("Positive")
elif num < 0 :
    print("Negative")
else:
    print("Zero")
