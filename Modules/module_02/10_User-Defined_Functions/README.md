# 🧑‍💻 User-Defined Functions in Python  

A **function** is like a **mini-machine** 🤖 inside your program.  
You give it something (input), it does some work, and it can give you something back (output).  

---

## 🔑 Key Concepts  

### 1. 🎯 Purpose of the Function  
- Every function has a **job**.  
- Example: A function can **add two numbers**.  

---

### 2. 🏷 Naming the Function  
- Give your function a **name** that tells what it does.  
- Example:  
```python
def add(num1, num2):   # "add" means it will add numbers
    return num1 + num2
```

---

### 3. 📥 Parameters (Inputs)
- Parameters = things you give to the function.
- Example:
```python
def add(num1, num2):   # num1 and num2 are inputs
    return num1 + num2
```

---


### 4. 📤 Returning the Output
- Functions can return something back.
- Example:
```python
def add(num1, num2):
    return num1 + num2   # gives back the sum
```

--- 

### 5. 📞 Calling the Function
- To use a function, you call it (like calling a friend 📱).
```python
result = add(2, 4)    # call function with 2 and 4
print(result)         # Output: 6
```