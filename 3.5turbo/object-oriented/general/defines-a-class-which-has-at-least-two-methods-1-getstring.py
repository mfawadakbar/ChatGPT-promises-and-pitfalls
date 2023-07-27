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
