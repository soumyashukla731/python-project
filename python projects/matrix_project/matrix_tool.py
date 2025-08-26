#import numpy library for matrix operation
import numpy as np

print("Welcome to Matrix Operations Tool!")

# get matrix input from user
def get_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))
    print(f"Enter values for Matrix {name}:")
    data = []
    for i in range(rows):
        row = input(f"Row {i+1} (separate numbers with spaces): ").split()
        data.append([int(x) for x in row])
    return np.array(data)

#select operation which user wants to perform
print("Select operation:")
print("1. Matrix Addition")
print("2. Matrix Subtraction")
print("3. Matrix Multiplication")
print("4. Matrix Transpose")
print("5. Matrix Determinant")
choice = input("Enter 1/2/3/4/5: ")

if choice == "1":
    A = get_matrix("A")
    B = get_matrix("B")
    print("Result:\n", A + B)
elif choice == "2":
    A = get_matrix("A")
    B = get_matrix("B")
    print("Result:\n", A - B)
elif choice == "3":
    A = get_matrix("A")
    B = get_matrix("B")
    print("Result:\n", np.dot(A, B))
elif choice == "4":
    A = get_matrix("A")
    print("Transpose:\n", A.T)
elif choice == "5":
    A = get_matrix("A")
    if A.shape == A.shape[11]:
        print("Determinant:", np.linalg.det(A))
    else:
        print("Determinant is only for square matrices!")
else:
    print("Invalid option.")
