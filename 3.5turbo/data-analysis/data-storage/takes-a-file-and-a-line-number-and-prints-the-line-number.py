Here is the python code that fulfills the given requirement:

```python
def print_line(file_name, line_number):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if line_number <= len(lines):
                line = lines[line_number - 1]
                print(line)
            else:
                print("Line number is out of range")
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    line_number = int(input("Enter the line number: "))
    print_line(file_name, line_number)
```

Explanation:
1. The `print_line` function takes the file name and line number as input.
2. It opens the file using `open()` in read mode.
3. It reads all the lines from the file using `readlines()`.
4. It checks if the given line number is within the range of available lines in the file.
5. If the line number is valid, it retrieves the line from the list of lines.
6. Otherwise, it prints an error message.
7. In the `main` function, it prompts the user to enter the file name and line number.
8. It converts the line number input to an integer using `int()`.
9. It calls the `print_line` function with the provided file name and line number.