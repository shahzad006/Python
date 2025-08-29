# 🔁 Python Loops
Loops are used to perform repetitive tasks efficiently. Python provides two types of loops:

- **For Loop**: Iterates over a sequence (e.g., list, tuple, dictionary).
- **While Loop**: Executes a block of code as long as a condition is true.

## 1️⃣ For Loop
👉 Used when you know how many times to repeat.  

```python
for i in range(5):
    print(i)  # 0,1,2,3,4
```
💡 `range(start, stop, step)` → control counting.

## 2️⃣ While Loop

👉 Repeats until condition is `False`.
```python
x = 1
while x <= 5:
    print(x)
    x += 1
```