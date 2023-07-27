Sure, here's a Python script that uses list comprehension to square each odd number in a list:

```python
# Get user input for a sequence of numbers
numbers = input("Enter a sequence of numbers (separated by spaces): ").split()

# Use list comprehension to square each odd number
squared_odd_numbers = [int(num)**2 for num in numbers if int(num) % 2 != 0]

# Print the squared odd numbers
print("Squared odd numbers:", squared_odd_numbers)
```

To run this script, save it with a `.py` extension (e.g., `task.py`) and execute it using the command `python task.py`. It will prompt the user to enter a sequence of numbers, separated by spaces, and then it will output the squared odd numbers from the input sequence.