Sure! Here's the python code that swaps the first and last elements in a list:

```python
def swap_first_and_last(lst):
    # Check if the list has at least two elements
    if len(lst) >= 2:
        # Swap first and last elements
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Test the function with some sample inputs
my_list = [1, 2, 3, 4, 5]
swapped_list = swap_first_and_last(my_list)
print(swapped_list)
```

Save the above code in a file named `task.py`, and run it using the command `python task.py`. It will swap the first and last elements of the list `[1, 2, 3, 4, 5]` and print the result.