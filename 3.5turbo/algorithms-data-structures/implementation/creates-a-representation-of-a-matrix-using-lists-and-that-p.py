Sure! Here's a Python script that creates a matrix using lists and provides functionality to add and delete rows:

```python
class Matrix:
    def __init__(self):
        self.matrix = []  # Initialize an empty matrix

    def add_row(self, row):
        """
        Add a new row to the matrix
        """
        self.matrix.append(row)

    def delete_row(self, index):
        """
        Delete a row from the matrix at the given index
        """
        if index < 0 or index >= len(self.matrix):
            raise IndexError("Invalid row index")

        del self.matrix[index]

    def display_matrix(self):
        """
        Display the current matrix
        """
        for row in self.matrix:
            print(row)

if __name__ == "__main__":
    matrix = Matrix()
    
    print("Enter the number of rows and columns for the matrix:")
    num_rows = int(input("Number of rows: "))
    num_cols = int(input("Number of columns: "))
    
    for _ in range(num_rows):
        row = []
        for j in range(num_cols):
            value = int(input(f"Enter value for row {_+1}, column {j+1}: "))
            row.append(value)
        matrix.add_row(row)
    
    print("\nMatrix:")
    matrix.display_matrix()

    choice = input("Do you want to add or delete a row? (add/delete/none): ")

    if choice == "add":
        row = []
        for j in range(num_cols):
            value = int(input(f"Enter value for the new row, column {j+1}: "))
            row.append(value)
        matrix.add_row(row)
        print("\nMatrix (after adding a row):")
        matrix.display_matrix()

    elif choice == "delete":
        index = int(input("Enter the index of the row to delete: "))
        matrix.delete_row(index)
        print("\nMatrix (after deleting a row):")
        matrix.display_matrix()

    else:
        print("\nMatrix (no changes):")
        matrix.display_matrix()
```

To run this script, save it in `task.py` and execute `python task.py` in the command prompt. You will be prompted to enter the number of rows and columns for the matrix, as well as the values for each element. After that, you can choose to add a new row, delete a row, or make no changes. The updated matrix will be displayed accordingly.