# ⚡ Exception Handling in Python  

Exception Handling = Gracefully handling unexpected issues (❌ wrong input, 🚫 missing files) **without crashing** the program.  
👉 Example: ATM shows “Invalid Amount” instead of shutting down.  

---

## 🔹 Types of Errors  

1. **Syntax Error** 📝  
Occurs **before execution** (wrong code structure).  
```python
print("Hello"   # ❌ Missing closing bracket

```

2. Runtime Error ⚙️
Occurs **during execution.**
```python
num = 10 / 0  # ❌ ZeroDivisionError
```

## 🔹 Try-Except Block
```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("❌ You cannot divide by zero!")

```

## 🔹 Handling Multiple Exceptions
```python
try:
    num1 = int(input("Enter first: "))
    num2 = int(input("Enter second: "))
    print("Result:", num1 / num2)
except ZeroDivisionError:
    print("🚫 Cannot divide by zero!")
except ValueError:
    print("⚠️ Invalid input! Numbers only.")

```

## 🔹 Generic Exception
```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except Exception as e:
    print("⚠️ Error occurred:", e)

```

## 🔹 Finally Block
```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("📂 File not found!")
finally:
    print("Closing file...")
    file.close()

```

## 🔹 Custom Exceptions
```python
def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative! ❌")
    print(f"Withdrawing ${amount}")

try:
    withdraw(-100)
except ValueError as e:
    print("⚠️ Error:", e)

```


## ✅ Best Practices
- 🔒 Always close files `(with open()` or `file.close()`)
- 🛡️ Use `try-except` for error resilience
- 💬 Give **clear error messages**
- 🚫 Avoid `except:` with no handling (silent failures)