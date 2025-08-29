# 🐍 Python Collections 
A **collection** = a box to keep many things together.

---

## 1️⃣ List 📦 (ordered, changeable)
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # apple
fruits.append("🍊")   # add orange
fruits[1] = "🍇"      # change banana
print(fruits)

```
✅ Ordered, can change, allows duplicates.

---

## 2️⃣ Tuple 🔒 (ordered, not changeable)
```python
point = (3, 5)
print(point[0])   # 3
# point[0] = 7 ❌ error
```
✅ Ordered, but locked (cannot change).

---

## 3️⃣ Set 🎨 (unordered, unique)
```python
colors = {"red", "blue", "green"}
colors.add("yellow")
print("red" in colors)  # True
```

✅ No duplicates, no order.

---

## 4️⃣ Dictionary 📖 (key → value)
```python
ages = {"Alice": 9, "Bob": 10}
print(ages["Alice"])    # 9
ages["Charlie"] = 8
```

✅ Key → Value pairs.

---

# ⚡ Cheat Sheet

- 📦 List `[]` → ordered, changeable

- 🔒 Tuple `()` → ordered, not changeable

- 🎨 Set `{}` → unique, unordered

- 📖 Dict `{"key": "value"}` → pairs