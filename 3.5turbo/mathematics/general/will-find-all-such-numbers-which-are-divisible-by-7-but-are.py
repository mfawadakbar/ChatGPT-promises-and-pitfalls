Sure! Here's a python script that finds all numbers divisible by 7 but not a multiple of 5:

```python
def find_numbers():
    numbers = []
    for num in range(1, 101):
        if num % 7 == 0 and num % 5 != 0:
            numbers.append(num)
    return numbers

if __name__ == "__main__":
    result = find_numbers()
    print(result)
```

This script defines a function `find_numbers()` that iterates through numbers from 1 to 100 (inclusive). It checks if a number is divisible by 7 but not a multiple of 5, then adds it to a list. Finally, it returns the list of numbers.

In the `if __name__ == "__main__"` block, we call the `find_numbers()` function and print the result.

You can run this script by saving it to a file called `task.py` and executing `python task.py` in the command line. It will print the numbers that satisfy the given condition.