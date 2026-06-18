# 🔢 Matrix Operations Tool
### QSkill Python Development Internship — Task 2
**Author:** Sourabh Saw | **GitHub:** [@Sourabhsaw1](https://github.com/Sourabhsaw1)

---

## 🎯 Objective
Create an interactive **Matrix Operations Tool** using Python and **NumPy** library that allows users to perform various matrix operations through a clean terminal interface.

---

## 📁 Project Structure
```
task2_project/
│
├── matrix_tool.py    ← Main Python script
└── README.md         ← This file
```

---

## 🛠️ Libraries Used
| Library | Purpose |
|---------|---------|
| `numpy` | All matrix operations & linear algebra |
| `os`    | Clear screen & terminal colors |

---

## ▶️ How to Run

```bash
# Step 1: Install numpy (if not installed)
pip install numpy

# Step 2: Run the tool
python matrix_tool.py
```

---

## ✨ Features

| # | Operation | Description |
|---|-----------|-------------|
| 1 | ➕ Addition | Add two matrices of same shape |
| 2 | ➖ Subtraction | Subtract two matrices of same shape |
| 3 | ✖️ Multiplication | Multiply matrices (cols of A = rows of B) |
| 4 | 🔄 Transpose | Flip rows and columns |
| 5 | 🔢 Determinant | Calculate determinant (square matrix only) |
| 6 | 🔁 Inverse | Find inverse matrix (non-singular only) |
| 7 | 📐 Eigenvalues | Calculate eigenvalues & eigenvectors |

---

## 🖥️ Sample Usage

```
╔══════════════════════════════════════╗
║     MATRIX OPERATIONS TOOL 🔢        ║
║     QSkill Internship - Task 2       ║
║     Author: Sourabh Saw              ║
╚══════════════════════════════════════╝

  Select Operation:
  1. ➕  Addition
  2. ➖  Subtraction
  3. ✖️   Multiplication
  4. 🔄  Transpose
  5. 🔢  Determinant
  6. 🔁  Inverse
  7. 📐  Eigenvalues & Eigenvectors
  0. 🚪  Exit
```

---

## 💡 Key NumPy Functions Used
- `np.add()` — Matrix addition
- `np.subtract()` — Matrix subtraction
- `np.matmul()` — Matrix multiplication
- `np.transpose()` — Transpose
- `np.linalg.det()` — Determinant
- `np.linalg.inv()` — Inverse
- `np.linalg.eig()` — Eigenvalues & Eigenvectors

---

## 🏢 Internship Details
- **Organization:** QSkill (Squarcell Resource India Pvt. Ltd)
- **Domain:** Python Development
- **Duration:** 1st June – 1st July 2026
- **Mode:** Virtual | **Stipend:** Unpaid
