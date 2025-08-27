# 🐍 Python Virtual Environments Guide  

## 1️⃣ What Are Virtual Environments?  
A **virtual environment** is an isolated Python workspace 🧑‍💻 where each project has its own interpreter + libraries 📦.  

🔑 **Why important?**  
- Project A needs `NumPy 1.3` 📉  
- Project B needs `NumPy 2.3` 📈  
👉 Without environments → conflicts ❌  
👉 With environments → smooth switching ✅  

---

## 2️⃣ Creating a Virtual Environment  
1. Open **Anaconda Prompt** 💻  
2. Navigate to project folder:  
```bash
cd Documents/Python/Projects

```
---
## 3️⃣ Create environment:
```bash
conda create -n firstenv python=3.10
```
✅ -n = name, python=3.10 = version

---

## 4️⃣ Activating & Using
- Activate:
```bash
conda activate firstenv
```
- Install packages:
```bash
pip install numpy==2.3   # pip
conda install pandas     # conda
```
- Check installed:
```bash
conda list

```

---

## 5️⃣Deactivate Environment
```bash
conda deactivate
```

---

## 6️⃣Manage Multiple Envs
- List all:
```bash
conda info --envs
```
- Delete env:
```bash
conda remove --name helloenv --all
```
---
## 7️⃣ Key Commands 📝

| Command | Description |
| ------ | ------ |
| `conda create -n <name> python=<ver>` | Create environment |
| `conda activate <name>` |Activate |
| `conda deactivate` | Deactivate |
| `conda list` | List all envs |
| `conda info --envs` | Show installed packages|
| `conda remove --name <name> --all` | Delete env |

