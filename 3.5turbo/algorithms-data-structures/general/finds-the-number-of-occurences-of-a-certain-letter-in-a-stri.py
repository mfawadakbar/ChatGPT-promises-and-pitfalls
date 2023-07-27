Here's the Python script to find the number of occurrences of a certain letter in a string:

```python
def count_occurrences(string, letter):
    """
    Function to count the number of occurrences of a letter in a string.

    Args:
        string (str): The input string.
        letter (str): The letter to count the occurrences of.

    Returns:
        int: The number of occurrences of the letter in the string.
    """
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

# Get user input for the string and the letter
string = input("Enter a string: ")
letter = input("Enter a letter: ")

# Call the function to count the occurrences
occurrences = count_occurrences(string, letter)

# Print the result
print("Number of occurrences of '{}' in '{}': {}".format(letter, string, occurrences))
```

To run the script, save it to a file called `task.py` and execute the command `python task.py`. The script will ask the user to enter a string and a letter, and then it will print the number of occurrences of the letter in the string.