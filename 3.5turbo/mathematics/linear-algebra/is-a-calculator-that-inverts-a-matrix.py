Sure! Here's a Python script that uses the NumPy library to invert a matrix:

```python
import numpy as np

def invert_matrix():
    # Get user input for the matrix size
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Get user input for the matrix elements
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            elem = float(input(f"Enter the element for position ({i+1},{j+1}): "))
            row.append(elem)
        matrix.append(row)

    # Convert the matrix to a NumPy array
    np_matrix = np.array(matrix)

    try:
        # Invert the matrix
        inv_matrix = np.linalg.inv(np_matrix)
        print("The inverted matrix is:")
        print(inv_matrix)
    except np.linalg.LinAlgError:
        print("Cannot invert the matrix as it is singular.")

if __name__ == '__main__':
    invert_matrix()
```

To run this script, save it in a file called `matrix_inverter.py`, and then open a terminal or command prompt and navigate to the directory where the file is located. Then simply run the command `python matrix_inverter.py`.

The script will ask you to enter the number of rows and columns for your matrix, and then prompt you to enter each element of the matrix. After you have provided all the matrix elements, it will calculate the inverse of the matrix using the `np.linalg.inv` function from the NumPy library, and display the inverted matrix. If the matrix is singular and cannot be inverted, it will display an error message instead.