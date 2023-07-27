Here's a Python script that compares the areas of a square and a circle:

```python
import math

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length**2

def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius**2

def compare_areas(square_side_length, circle_radius):
    """Compare the areas of a square and a circle."""
    square_area = calculate_square_area(square_side_length)
    circle_area = calculate_circle_area(circle_radius)

    if square_area > circle_area:
        return "Square has a larger area."
    elif square_area < circle_area:
        return "Circle has a larger area."
    else:
        return "Both square and circle have the same area."

if __name__ == "__main__":
    # Get user input for side length and radius
    side_length = float(input("Enter the side length of the square: "))
    radius = float(input("Enter the radius of the circle: "))

    # Compare areas
    result = compare_areas(side_length, radius)
    print(result)
```

Save this script in a file named `task.py` and run it with the command `python task.py`. The script will ask the user to enter the side length of a square and the radius of a circle, and then compare the areas of the two shapes. The result will be displayed as output.