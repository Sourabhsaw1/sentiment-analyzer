# ============================================================
# QSkill Internship - Task 2: Matrix Operations Tool
# Author  : Sourabh Saw
# GitHub  : https://github.com/Sourabhsaw1
# Library : NumPy
# ============================================================

import numpy as np
import os

# ── Colors for terminal (Windows compatible) ─────────────────
class Color:
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ============================================================
# DISPLAY MATRIX — nicely formatted
# ============================================================
def display_matrix(matrix, title="Matrix"):
    print(f"\n{Color.CYAN}{Color.BOLD}  {title}:{Color.RESET}")
    print(f"{Color.YELLOW}", end="")
    # Find max width for alignment
    max_w = max(len(f"{val:.2f}") for row in matrix for val in row)
    print("  ┌" + "─" * (max_w * matrix.shape[1] + matrix.shape[1] * 2 + 1) + "┐")
    for row in matrix:
        print("  │ ", end="")
        for val in row:
            print(f"{val:>{max_w}.2f} ", end="")
        print("│")
    print("  └" + "─" * (max_w * matrix.shape[1] + matrix.shape[1] * 2 + 1) + "┘")
    print(Color.RESET, end="")

# ============================================================
# INPUT MATRIX from user
# ============================================================
def input_matrix(name="Matrix"):
    print(f"\n{Color.CYAN}  Enter {name}:{Color.RESET}")
    while True:
        try:
            rows = int(input(f"  Rows    : "))
            cols = int(input(f"  Columns : "))
            if rows <= 0 or cols <= 0:
                print(f"{Color.RED}  ❌ Rows and columns must be positive!{Color.RESET}")
                continue
            break
        except ValueError:
            print(f"{Color.RED}  ❌ Enter valid numbers!{Color.RESET}")

    print(f"  Enter elements row by row (space separated):")
    data = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"  Row {i+1}  : ").split()
                if len(row_input) != cols:
                    print(f"{Color.RED}  ❌ Enter exactly {cols} values!{Color.RESET}")
                    continue
                data.append([float(x) for x in row_input])
                break
            except ValueError:
                print(f"{Color.RED}  ❌ Enter valid numbers only!{Color.RESET}")

    return np.array(data)

# ============================================================
# OPERATIONS
# ============================================================

def addition():
    print(f"\n{Color.BOLD}  ── MATRIX ADDITION ──{Color.RESET}")
    A = input_matrix("Matrix A")
    B = input_matrix("Matrix B")
    if A.shape != B.shape:
        print(f"{Color.RED}  ❌ Shapes don't match! A:{A.shape} B:{B.shape}{Color.RESET}")
        return
    result = np.add(A, B)
    display_matrix(A, "Matrix A")
    display_matrix(B, "Matrix B")
    display_matrix(result, "A + B (Result)")
    print(f"{Color.GREEN}  ✅ Addition successful!{Color.RESET}")


def subtraction():
    print(f"\n{Color.BOLD}  ── MATRIX SUBTRACTION ──{Color.RESET}")
    A = input_matrix("Matrix A")
    B = input_matrix("Matrix B")
    if A.shape != B.shape:
        print(f"{Color.RED}  ❌ Shapes don't match! A:{A.shape} B:{B.shape}{Color.RESET}")
        return
    result = np.subtract(A, B)
    display_matrix(A, "Matrix A")
    display_matrix(B, "Matrix B")
    display_matrix(result, "A - B (Result)")
    print(f"{Color.GREEN}  ✅ Subtraction successful!{Color.RESET}")


def multiplication():
    print(f"\n{Color.BOLD}  ── MATRIX MULTIPLICATION ──{Color.RESET}")
    print(f"{Color.YELLOW}  Note: Columns of A must equal Rows of B{Color.RESET}")
    A = input_matrix("Matrix A")
    B = input_matrix("Matrix B")
    if A.shape[1] != B.shape[0]:
        print(f"{Color.RED}  ❌ Invalid shapes! A:{A.shape} B:{B.shape}")
        print(f"  Columns of A ({A.shape[1]}) must equal Rows of B ({B.shape[0]}){Color.RESET}")
        return
    result = np.matmul(A, B)
    display_matrix(A, "Matrix A")
    display_matrix(B, "Matrix B")
    display_matrix(result, "A × B (Result)")
    print(f"{Color.GREEN}  ✅ Multiplication successful!{Color.RESET}")


def transpose():
    print(f"\n{Color.BOLD}  ── MATRIX TRANSPOSE ──{Color.RESET}")
    A = input_matrix("Matrix A")
    result = np.transpose(A)
    display_matrix(A, "Original Matrix")
    display_matrix(result, "Transposed Matrix")
    print(f"{Color.GREEN}  ✅ Transpose successful!{Color.RESET}")
    print(f"  Shape changed: {A.shape} → {result.shape}")


def determinant():
    print(f"\n{Color.BOLD}  ── MATRIX DETERMINANT ──{Color.RESET}")
    print(f"{Color.YELLOW}  Note: Only square matrices (NxN) have determinant{Color.RESET}")
    A = input_matrix("Matrix A")
    if A.shape[0] != A.shape[1]:
        print(f"{Color.RED}  ❌ Matrix must be square! Got: {A.shape}{Color.RESET}")
        return
    det = np.linalg.det(A)
    display_matrix(A, "Matrix A")
    print(f"\n{Color.GREEN}  ✅ Determinant = {det:.4f}{Color.RESET}")
    if abs(det) < 1e-10:
        print(f"{Color.YELLOW}  ⚠️  Determinant ≈ 0 → Matrix is Singular (not invertible){Color.RESET}")


def inverse():
    print(f"\n{Color.BOLD}  ── MATRIX INVERSE ──{Color.RESET}")
    print(f"{Color.YELLOW}  Note: Only square non-singular matrices have inverse{Color.RESET}")
    A = input_matrix("Matrix A")
    if A.shape[0] != A.shape[1]:
        print(f"{Color.RED}  ❌ Matrix must be square! Got: {A.shape}{Color.RESET}")
        return
    det = np.linalg.det(A)
    if abs(det) < 1e-10:
        print(f"{Color.RED}  ❌ Matrix is Singular (det=0), inverse doesn't exist!{Color.RESET}")
        return
    result = np.linalg.inv(A)
    display_matrix(A, "Original Matrix")
    display_matrix(result, "Inverse Matrix (A⁻¹)")
    print(f"{Color.GREEN}  ✅ Inverse calculated successfully!{Color.RESET}")


def eigenvalues():
    print(f"\n{Color.BOLD}  ── EIGENVALUES & EIGENVECTORS ──{Color.RESET}")
    print(f"{Color.YELLOW}  Note: Only for square matrices{Color.RESET}")
    A = input_matrix("Matrix A")
    if A.shape[0] != A.shape[1]:
        print(f"{Color.RED}  ❌ Matrix must be square!{Color.RESET}")
        return
    vals, vecs = np.linalg.eig(A)
    display_matrix(A, "Matrix A")
    print(f"\n{Color.CYAN}{Color.BOLD}  Eigenvalues:{Color.RESET}")
    for i, v in enumerate(vals):
        print(f"  λ{i+1} = {v:.4f}")
    display_matrix(np.real(vecs), "Eigenvectors (columns)")
    print(f"{Color.GREEN}  ✅ Done!{Color.RESET}")

# ============================================================
# MAIN MENU
# ============================================================
def print_menu():
    print(f"""
{Color.BOLD}{Color.CYAN}
  ╔══════════════════════════════════════╗
  ║     MATRIX OPERATIONS TOOL 🔢        ║
  ║     QSkill Internship - Task 2       ║
  ║     Author: Sourabh Saw              ║
  ╚══════════════════════════════════════╝
{Color.RESET}
  {Color.YELLOW}Select Operation:{Color.RESET}

  {Color.GREEN}1.{Color.RESET} ➕  Addition
  {Color.GREEN}2.{Color.RESET} ➖  Subtraction
  {Color.GREEN}3.{Color.RESET} ✖️   Multiplication
  {Color.GREEN}4.{Color.RESET} 🔄  Transpose
  {Color.GREEN}5.{Color.RESET} 🔢  Determinant
  {Color.GREEN}6.{Color.RESET} 🔁  Inverse
  {Color.GREEN}7.{Color.RESET} 📐  Eigenvalues & Eigenvectors
  {Color.RED}0.{Color.RESET} 🚪  Exit
""")

def main():
    # Enable ANSI colors on Windows
    os.system("")

    operations = {
        "1": addition,
        "2": subtraction,
        "3": multiplication,
        "4": transpose,
        "5": determinant,
        "6": inverse,
        "7": eigenvalues,
    }

    while True:
        clear()
        print_menu()
        choice = input(f"  {Color.BOLD}Enter choice (0-7): {Color.RESET}").strip()

        if choice == "0":
            print(f"\n{Color.GREEN}  👋 Thanks for using Matrix Operations Tool!{Color.RESET}\n")
            break
        elif choice in operations:
            operations[choice]()
            input(f"\n  {Color.YELLOW}Press Enter to continue...{Color.RESET}")
        else:
            print(f"{Color.RED}  ❌ Invalid choice! Enter 0-7{Color.RESET}")
            input(f"\n  Press Enter to continue...")

if __name__ == "__main__":
    main()
