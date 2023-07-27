Sure! Here is a Python script that defines a class with a generator to iterate the numbers divisible by 7:

```python
class DivisibleBySevenGenerator:
    def __init__(self, start=0, end=None):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start is None:
            raise StopIteration

        current_number = self.start
        if self.end and current_number > self.end:
            raise StopIteration

        while current_number % 7 != 0:
            current_number += 1

        self.start = current_number + 7
        return current_number

if __name__ == "__main__":
    # Testing the generator
    generator = DivisibleBySevenGenerator()
    for number in generator:
        if number > 100:
            break
        print(number)
```

To run the script, save it in a file called `task.py` and use the command `python task.py` in your terminal. It will print all the numbers divisible by 7 up to 100. You can modify the `start` and `end` parameters in the `DivisibleBySevenGenerator` constructor to generate numbers within a specific range, or leave them as default to generate an infinite sequence.