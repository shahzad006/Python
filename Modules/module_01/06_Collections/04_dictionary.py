student = {
    "name": "Ali",
    "age": 9,
    "grade": "4th"
}

print(student)

# ---------------------------------------------------------------------------- #

print(student["name"])      # Ali
print(student.get("age"))   # 9

# ---------------------------------------------------------------------------- #

student["age"] = 10
print(student)

# ---------------------------------------------------------------------------- #

student["school"] = "City School"
print(student)

# ---------------------------------------------------------------------------- #

student.pop("grade")    # removes key "grade"
print(student)

# ---------------------------------------------------------------------------- #

student.clear()         # makes dictionary empty
print(student)


# ---------------------------------------------------------------------------- #

students = {
    "student1": {"name": "Ali", "age": 9},
    "student2": {"name": "Sara", "age": 8}
}

print(students["student1"]["name"])  # Ali
