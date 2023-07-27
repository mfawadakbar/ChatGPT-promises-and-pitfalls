Sure! Here's a Python script that generates a dictionary based on an integral number `n`:

```python
def generate_dictionary(n):
    # Initialize an empty dictionary
    dictionary = {}

    # Iterate from 1 to n
    for i in range(1, n+1):
        # If i is divisible by 2, add it as key in the dictionary
        if i % 2 == 0:
            dictionary[i] = i**2
        # If i is not divisible by 2, add it as key and the square of i as value in the dictionary
        else:
            dictionary[i] = i**3
    
    return dictionary

if __name__ == '__main__':
    # Get user input for n
    n = int(input("Enter an integral number: "))
    
    # Generate the dictionary
    result = generate_dictionary(n)
    
    # Print the dictionary
    print(result)
```

This script defines a function `generate_dictionary` that generates a dictionary according to the given criteria. It then prompts the user to enter an integral number `n`, generates the dictionary using the `generate_dictionary` function, and prints the resulting dictionary.

To run the script, save it into a file named `task.py` and simply run `python task.py` in the command line.