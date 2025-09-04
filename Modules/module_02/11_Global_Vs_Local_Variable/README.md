# 🔑 Key Concepts: Local vs Global Variables in Python

## 📝 Local Variables
- A **local variable** is created inside a **function**.
- It only works **inside that function.**
- Outside the function, Python cannot see it.

***👉 Analogy:***
Think of a classroom whiteboard. Only the students in that classroom can see what’s written.

### Example:
```python
def my_function():
    y = 5  # Local variable
    print("Inside function: y =", y)

my_function()
# print(y)  # ❌ Error: y is not defined outside

```

## 📊 Diagram (Local Variable Scope):

```python
+--------------------------+
|  Function: my_function() |
|   y = 5  (local)         |
+--------------------------+

Outside function ❌  y not visible

```

## 🌍 Global Variables
- A global variable is created outside any function
- It can be used everywhere in the program.
***👉 Analogy:***
Think of the school’s notice board. Everyone in the school can see it, not just one class.
### Example:
```python
x = 10  # Global variable

def my_function():
    print("Inside function: x =", x)

my_function()
print("Outside function: x =", x)
```

## 📊 Diagram (Global Variable Scope):
```python
x = 10 (global)

+--------------------------+
|  Function: my_function() |
|   can use x              |
+--------------------------+

Outside function ✅  x visible

```

## ⚖️ Local vs Global in Action
```python 
x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    print("Inside function: x =", x, "y =", y)

my_function()

print("Outside function: x =", x)
# print("Outside function: y =", y)  # ❌ Error: y not defined

```