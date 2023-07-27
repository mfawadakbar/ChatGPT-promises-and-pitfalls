Sure! Here's a Python script that calculates the mean, median, mode, and range of a list of numbers without using any libraries:

```python
def find_mean(numbers):
    total = sum(numbers)
    return total / len(numbers)

def find_median(numbers):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        middle = length // 2
        return (numbers[middle-1] + numbers[middle]) / 2
    else:
        middle = length // 2
        return numbers[middle]

def find_mode(numbers):
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_count = max(count_dict.values())
    mode = [k for k, v in count_dict.items() if v == max_count]
    return mode

def find_range(numbers):
    return max(numbers) - min(numbers)

# Ask user for a list of numbers
input_numbers = input("Enter a list of numbers, separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

# Calculate mean, median, mode, and range
mean = find_mean(numbers)
median = find_median(numbers)
mode = find_mode(numbers)
range_ = find_range(numbers)

# Print the results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Range:", range_)
```

To run this script, save it to a file called `task.py`, then open a terminal or command prompt, navigate to the directory containing the file, and run the command `python task.py`. You will be prompted to enter a list of numbers, separated by spaces. After entering the numbers, the script will calculate and display the mean, median, mode, and range.