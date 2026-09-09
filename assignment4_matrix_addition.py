# PRN      : 1272261997
# Name     : Sujeet Kapoor
# Division : 9
# Branch   : CSE (AI-DS)
# Subject  : Python
# Assignment 4 : Create an array and perform addition of two matrices


def read_matrix(name, rows, cols):
    """Reads a matrix of the given size from the user and returns it."""
    print(f"\nEnter the elements of the {name} matrix, row by row:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Element [{i+1}][{j+1}] : "))
            row.append(value)
        matrix.append(row)
    return matrix


def add_matrices(m1, m2, rows, cols):
    """Adds two matrices of the same size and returns the result."""
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result


def display_matrix(heading, matrix):
    """Prints a matrix in a neat grid."""
    print("\n" + heading)
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


# ---------- Main program ----------

print("Matrix Addition")
print("---------------")

rows = int(input("Enter the number of rows    : "))
cols = int(input("Enter the number of columns : "))

# An array (matrix) here is a list of lists.
# Each inner list is one row of the matrix.
matrix1 = read_matrix("FIRST", rows, cols)
matrix2 = read_matrix("SECOND", rows, cols)

result = add_matrices(matrix1, matrix2, rows, cols)

display_matrix("First Matrix:", matrix1)
display_matrix("Second Matrix:", matrix2)
display_matrix("Sum of the two matrices:", result)
