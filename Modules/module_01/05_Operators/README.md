# ⚙️ Python Operators

## 1️⃣ Assignment Operators
- `=` Assign → `x = 5`  
- `+=` Add & Assign → `x += 3` → `x = x + 3`  

```python
x = 5
x += 3
print(x)  # 8
```
---

##  2️⃣Arithmetic Operators
- ➕ `+` Add → `5 + 3 = 8`  
- ➖ `-` Subtract → `5 - 3 = 2`  
- ✖️ `*` Multiply → `5 * 3 = 15`  
- ➗ `/` Division → `10 / 3 = 3.33` (float)  
- 🪙 `%` Modulus → `10 % 3 = 1` (remainder)  
- 🔼 `**` Exponent → `2 ** 3 = 8`  
- 🧮 `//` Floor Division → `10 // 3 = 3` (no decimals)  

💡 **Difference:** `/` gives float, `//` gives integer.

---
## 3️⃣ Comparison Operators
- > Greater → `5 > 3 ✅`
- < Less → `5 < 3 ❌`
- == Equal → `5 == 5 ✅`
- != Not Equal → `5 != 3 ✅`
- >= Greater/Equal
- <= Less/Equal

```python
x, y = 5, 10
print(x > y)   # False
print(x != y)  # True
```
---

## 4️⃣ Logical Operators

- and → True if both true
- or → True if at least one true
- not → Reverses value
```python
a, b = True, False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```