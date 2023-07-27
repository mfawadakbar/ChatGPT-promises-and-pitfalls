Sure! Here's a Python script that checks whether a string is a palindrome or symmetrical.

```python
def is_palindrome(string):
    # Remove whitespace and convert the string to lowercase
    string = string.replace(" ", "").lower()
    length = len(string)

    # Check if the string is symmetrical
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            return False

    return True


if __name__ == "__main__":
    # Get user input
    string = input("Enter a string: ")

    if is_palindrome(string):
        print("The string is a palindrome or symmetrical.")
    else:
        print("The string is not a palindrome or symmetrical.")
```

To run this script, save it in a file called `task.py` and run `python task.py` in the terminal. The script will ask for user input and then determine whether the input string is a palindrome or symmetrical.