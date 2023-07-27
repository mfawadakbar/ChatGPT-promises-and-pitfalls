Certainly! Below is a python script that generates a specified number of random numbers and stores them in a file called "random_numbers.txt". The script uses the random module in Python to generate random numbers.

```python
import random

def generate_random_numbers(num_of_numbers):
    """Generates random numbers and stores them in a file"""
    random_numbers = []
    for _ in range(num_of_numbers):
        random_numbers.append(random.randint(1, 100))
    
    with open("random_numbers.txt", "w") as file:
        for number in random_numbers:
            file.write(str(number) + "\n")
    print(f"{num_of_numbers} random numbers generated and saved in random_numbers.txt")

# Prompt the user to enter the number of random numbers to generate
num_of_numbers = int(input("Enter the number of random numbers to generate: "))

generate_random_numbers(num_of_numbers)
```

Simply save the above code in a file called "task.py" and execute it using the command `python task.py`. It will prompt the user to enter the number of random numbers to generate and store them in the "random_numbers.txt" file.