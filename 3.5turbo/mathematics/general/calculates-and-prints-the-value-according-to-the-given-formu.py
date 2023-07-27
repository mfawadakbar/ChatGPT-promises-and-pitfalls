Sure! Here's a Python script that calculates and prints the value according to the given formula:

```python
import math

def calculate_value():
    # Ask the user for input values
    C = float(input("Enter the value of C: "))
    D = float(input("Enter the value of D: "))
    H = float(input("Enter the value of H: "))

    # Calculate the value according to the formula
    Q = math.sqrt((2 * C * D) / H)

    # Print the result
    print("The calculated value is:", Q)

if __name__ == "__main__":
    calculate_value()
```

To run this script, save it in a file named `task.py` and then execute the command `python task.py` in your terminal. The script will prompt you to enter the values of C, D, and H, and then it will calculate and print the result.