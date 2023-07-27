Sure! Here's a Python script that uses recursion to find the nth Fibonacci number:

```python
def fibonacci(n):
    """
    Recursive function to find the nth Fibonacci number
    
    Args:
        n (int): The position of the Fibonacci number
        
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 0:
        return "Invalid input. n should be a positive integer."

    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """
    Main function to get user input and print the nth Fibonacci number
    """

    # Get user input
    try:
        n = int(input("Enter the position of the Fibonacci number: "))
    except ValueError:
        print("Invalid input. n should be a positive integer.")
        return

    # Calculate the nth Fibonacci number
    fib = fibonacci(n)

    # Print the result
    print(f"The {n}th Fibonacci number is: {fib}")


if __name__ == "__main__":
    main()
```

Save this script in a file named `task.py`, and you can run it using the command `python task.py`. The script will ask you to enter the position of the Fibonacci number, and it will output the result.

Note: The Fibonacci sequence starts with 1, so the first Fibonacci number is 1, the second is 1, the third is 2, and so on.