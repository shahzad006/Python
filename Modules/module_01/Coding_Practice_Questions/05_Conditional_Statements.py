
# ---------------------------------------------------------------------------- #
#                            Conditional Statements                            #
# ---------------------------------------------------------------------------- #

#* Q1: Even or Odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# ---------------------------------------------------------------------------- #


#* Q2: Prime number check

num = int(input("Enter a number: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime")
else:
    print("Not Prime")




# ---------------------------------------------------------------------------- #



#* Q3: Adult or Minor


age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")




# ---------------------------------------------------------------------------- #



#* Q4: Largest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)



# ---------------------------------------------------------------------------- #

#* Q5: Leap year check

year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")




# ---------------------------------------------------------------------------- #


#* Q6: Grading system

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")


# ---------------------------------------------------------------------------- #


#* Q7: ATM Transaction

balance = 1000
withdraw = int(input("Enter withdrawal amount: "))
if withdraw <= balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")



# ---------------------------------------------------------------------------- #


#* Q8: Password check

password = input("Enter password: ")
if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")


# ---------------------------------------------------------------------------- #


#* Q9: Number guessing game


secret = 7
guess = int(input("Guess the number: "))
if guess == secret:
    print("Correct! 🎉")
else:
    print("Wrong! Try again.")




# ---------------------------------------------------------------------------- #


#* Q10: Temperature check


temp = int(input("Enter temperature: "))
if temp > 30:
    print("Hot")
elif temp >= 15:
    print("Warm")
else:
    print("Cold")
