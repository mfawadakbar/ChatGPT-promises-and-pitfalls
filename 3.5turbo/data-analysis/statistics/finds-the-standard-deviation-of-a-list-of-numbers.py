Sure! Here is a Python script that calculates the standard deviation of a given list of numbers using the `statistics` library:

```python
import statistics

def calculate_std_deviation(numbers):
    return statistics.stdev(numbers)

if __name__ == '__main__':
    # Get input from the user
    num_list = input("Enter a list of numbers (separated by space): ").split()

    # Convert input to list of floats
    try:
        num_list = list(map(float, num_list))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        exit()

    # Calculate standard deviation
    std_deviation = calculate_std_deviation(num_list)
    print(f"The standard deviation of the given numbers is: {std_deviation}")
```

To run this script, create a file named `task.py` and copy the above code into it. Then, open a terminal, navigate to the directory where the file is located, and execute `python task.py`. The script will prompt you to enter a list of numbers, separated by spaces. After you provide the input, it will calculate and display the standard deviation of the numbers.