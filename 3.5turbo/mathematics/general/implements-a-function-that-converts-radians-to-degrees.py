Sure! Here's the solution:

```python
import math

def convert_radians_to_degrees(radians):
    """
    Convert radians to degrees.
    """
    degrees = math.degrees(radians)
    return degrees

if __name__ == '__main__':
    radians = float(input("Enter the value in radians: "))
    degrees = convert_radians_to_degrees(radians)
    print(f"{radians} radians is equal to {degrees} degrees.")
```

Please save the code in a file named `task.py` and run it using the command `python task.py`. The script will ask you to enter a value in radians, and it will then convert it to degrees and display the result.