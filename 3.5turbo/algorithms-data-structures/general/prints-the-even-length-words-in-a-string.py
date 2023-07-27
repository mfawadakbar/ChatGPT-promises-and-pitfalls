Sure! Here's the Python code to print the even length words in a string:

```python
def print_even_length_words(string):
    # Split the string into words
    words = string.split()

    # Iterate over the words and print the even length words
    for word in words:
        if len(word) % 2 == 0:
            print(word)

# Ask the user to input a string
user_input = input("Enter a string: ")

# Call the function to print the even length words
print_even_length_words(user_input)
```

To run this code, save it in a file named `task.py` and execute it using the command `python task.py`. The script will prompt you to enter a string, and it will then print the even length words in that string.