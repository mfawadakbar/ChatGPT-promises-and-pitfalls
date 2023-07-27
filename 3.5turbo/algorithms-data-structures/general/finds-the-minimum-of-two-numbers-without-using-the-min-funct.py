Here's a python code that finds the minimum of two numbers without using the `min` function:

```python
def find_minimum(a, b):
    # Check if a is less than b
    if a < b:
        return a
    # Otherwise, b is the minimum
    else:
        return b


# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and print the result
minimum = find_minimum(num1, num2)
print("The minimum is:", minimum)
```

This code defines a function `find_minimum` that takes two numbers as input and returns the minimum of the two numbers. It compares the two numbers using the less than operator and returns the appropriate value.

Then, it prompts the user to enter the two numbers, stores them in variables `num1` and `num2`, and calls the `find_minimum` function to find the minimum. Finally, it prints out the minimum value.

You can run this script by saving it in a file called "task.py" and executing the command `python task.py` in the terminal.