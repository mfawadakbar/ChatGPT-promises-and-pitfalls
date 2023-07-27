Sure! Here's a Python script that takes a tuple representing an RGB value and returns its inverted value:

```python
def invert_rgb(rgb):
    """
    Function to invert an RGB value represented by a tuple.

    Arguments:
    rgb -- Tuple representing an RGB value

    Returns:
    Tuple representing the inverted RGB value
    """
    inverted_rgb = tuple(255 - value for value in rgb)
    return inverted_rgb


# Test case
rgb_value = (164, 194, 244)
inverted_rgb_value = invert_rgb(rgb_value)
print(f"Inverted RGB value: {inverted_rgb_value}")
```

This script defines a function `invert_rgb` that takes a tuple `rgb` as an argument. It then calculates the inverted RGB value by subtracting each value in the tuple from 255. The inverted RGB value is returned as a tuple.

In the test case, the script creates a tuple `rgb_value` representing the RGB value (164, 194, 244) and passes it to the `invert_rgb` function. The inverted RGB value is then printed to the console.

To run the script, save it in a file named `task.py` and run `python task.py` in the command line.