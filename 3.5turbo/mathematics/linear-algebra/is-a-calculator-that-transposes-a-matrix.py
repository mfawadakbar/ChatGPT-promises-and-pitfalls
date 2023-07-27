Sure! Here's a Python script that transposes a matrix:

```python
import numpy as np

def transpose_matrix():
    # Get the number of rows and columns in the matrix from the user
    num_rows = int(input("Enter the number of rows in the matrix: "))
    num_cols = int(input("Enter the number of columns in the matrix: "))
    
    # Initialize an empty matrix
    matrix = []
    
    # Get the matrix elements from the user
    print("Enter the matrix elements row by row:")
    for _ in range(num_rows):
        row = input().split()
        row = [float(element) for element in row]
        matrix.append(row)
    
    # Transpose the matrix using numpy
    transposed_matrix = np.transpose(matrix)
    
    # Print the transposed matrix
    print("Transposed matrix:")
    for row in transposed_matrix:
        print(row)

if __name__ == "__main__":
    transpose_matrix()
```

This script asks the user to enter the number of rows and columns in the matrix, and then takes input for each element of the matrix row by row. It uses the NumPy library to transpose the matrix and then prints the transposed matrix. The user can run the script by executing the command `python task.py`.