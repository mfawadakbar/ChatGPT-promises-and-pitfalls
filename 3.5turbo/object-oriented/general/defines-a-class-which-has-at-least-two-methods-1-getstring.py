Sure, here is the code for the requested class:

```python
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())


if __name__ == "__main__":
    # Create an instance of the StringManipulator class
    stringManipulator = StringManipulator()

    # Get a string from console input
    stringManipulator.getString()

    # Print the string in upper case
    stringManipulator.printString()
```

To run this code, save it in a file called "task.py". Open your command prompt or terminal, navigate to the folder where "task.py" is saved, and enter the command `python task.py`. The code will prompt you to enter a string, and then it will print that string in uppercase.