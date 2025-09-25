# ---------------------------------------------------------------------------- #
#                                 File handling                                #
# ---------------------------------------------------------------------------- #


# ------------------------------------ "R" ----------------------------------- #

f = open("file.txt" , "r")


# Read the content of the file
content = f.read()
print(content)

# First line read
content = f.readline()
print(content)


# Read all lines
content = f.readlines()
print(content)


# ---------------------------------------------------------------------------- #

# ------------------------------------ "W" ----------------------------------- #

# Create a new file or overwrite an existing file
f = open("file.txt" , "w")
f.write("This is a new line\n")
f.close()



# ---------------------------------------------------------------------------- #

# ------------------------------------ "A" ----------------------------------- #

# Append to an existing file
f = open("file.txt" , "a")
f.write("Python Programming\n")
f.write("Topic File handling\n")

f.close()


# ---------------------------------------------------------------------------- #

# ----------------------------------- "R+" ----------------------------------- #

f = open("file.txt" , "r+")
content = f.read()
print(content)
f.write("This is a new line\n")
f.close()


# ---------------------------------------------------------------------------- #


# ----------------------------------- With ----------------------------------- #

with open("file.txt" , "r") as f:
    content = f.read()
    print(content)


# No need to close the file, it will be closed automatically

with open("file.txt" , "w") as f:
    f.write("This is a new line\n") 
    f.write("Python Programming\n")
    f.write("Topic File handling\n")



# ---------------------------------------------------------------------------- #


# -------------------------------- delete_file ------------------------------- #

import os

os.remove("file.txt")


