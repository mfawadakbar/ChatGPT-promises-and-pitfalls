Sure, here's a Python script that finds the maximum of two numbers without using the max function:

```python
def get_max(num1, num2):
    """
    Function to find the maximum of two numbers.
    """
    if num1 >= num2:
        return num1
    else:
        return num2

# Getting input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function to find the maximum of two numbers
result = get_max(num1, num2)

# Printing the maximum number
print("The maximum number is:", result)
```

Save the script in a file named "task.py" and you can run it using the command `python task.py`. It will ask you to enter two numbers, and then it will display the maximum of those two numbers.