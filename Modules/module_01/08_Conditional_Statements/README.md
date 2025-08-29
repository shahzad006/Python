# ⚡ Python Conditional Statements

## 1️⃣ Why Do We Need Them?
👉 To make decisions in code based on conditions.  
💡 Real-life:
- ☔ If it rains → take umbrella  
- 🚦 If light is green → go, else stop  
- 🔑 If password correct → login, else deny  

---

## 2️⃣ Basic Conditionals
### 🔹 if
```python
traffic_light = "green"
if traffic_light == "green":
    print("You can go ✅")
```

### 🔹 if...else
```python
traffic_light = "red"
if traffic_light == "green":
    print("You can go ✅")
else:
    print("You must stop ⛔")

```

### 🔹 if...elif...else
```python
traffic_light = "yellow"
if traffic_light == "green":
    print("Go ✅")
elif traffic_light == "yellow":
    print("Slow down ⚠️")
else:
    print("Stop ⛔")

```

## 3️⃣ Nested Conditions 🌀
```python
car_speed = 60
seat_belt = True

if car_speed <= 60:
    if seat_belt:
        print("Driving safely 🚗✅")
    else:
        print("Wear seat belt! 🎯")
else:
    print("Too fast! 🏎️⚠️")

```

## 4️⃣ Logical Operators 🔀

- `and` → both must be true

- `or` → at least one true

- `not` → reverses condition

```python
vehicle = "ambulance"
light = "red"

if light == "green" or vehicle == "ambulance":
    print("You can go 🚑✅")

```

## 5️⃣ Case Sensitivity 🔡
```python
traffic_light = "Red"
if traffic_light == "red":
    print("Stop ⛔")
else:
    print("Slow down ⚠️")

```