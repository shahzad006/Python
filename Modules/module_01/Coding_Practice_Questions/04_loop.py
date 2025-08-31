
# ---------------------------------------------------------------------------- #
#                                     Loop                                     #
# ---------------------------------------------------------------------------- #

#* Q1: Print numbers 1 to 20 (for loop)


for i in range(1, 21):
    print(i)


# ---------------------------------------------------------------------------- #

#* Q2: Print numbers 1 to 20 (while loop)


num = 0 

while num < 21:
    print(num )
    num += 1


# ---------------------------------------------------------------------------- #

#* Q3: Print multiplication table of a number

table = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")




# ---------------------------------------------------------------------------- #


#* Q4: Even numbers 1–100

for i in range(2, 101, 2):
    print(i)



# ---------------------------------------------------------------------------- #

#* Q5: Odd numbers 1–100

for i in range(1, 101, 2):
    print(i)



# ---------------------------------------------------------------------------- #

#* Q6: Sum of numbers 1–50

num = 0 

for i in range(1, 51):
    num += i
print(num)



# ---------------------------------------------------------------------------- #

#* Q7: Factorial of a number


num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial =", fact)


# ---------------------------------------------------------------------------- #

#* Q8: Print each character of "PYTHON"


for ch in "PYTHON":
    print(ch)

# ---------------------------------------------------------------------------- #

#* Q9: Reverse a string using loop


text = "PYTHON"
rev = ""
for ch in text:
    rev = ch + rev
print("Reversed:", rev)


# ---------------------------------------------------------------------------- #

#* Q10: Nested loops - 3x3 star pattern

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


