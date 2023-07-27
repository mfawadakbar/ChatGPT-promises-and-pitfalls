Sure! Here's a Python script that calculates the missing side length in a right triangle using the Pythagorean theorem:

```python
import math

def pythagorean_theorem():
    # Get the lengths of the two known sides from the user
    side_a = float(input("Enter the length of side A: "))
    side_b = float(input("Enter the length of side B: "))
    
    # Calculate the length of the missing side (side C)
    side_c = math.sqrt(side_a**2 + side_b**2)
    
    # Print the result
    print(f"The length of side C is {side_c:.2f}")

# Run the function
pythagorean_theorem()
```

Explanation:
1. The script imports the `math` library, which provides mathematical functions.
2. The `pythagorean_theorem` function asks the user to enter the lengths of side A and side B.
3. The function then calculates the missing side (side C) using the Pythagorean theorem formula: C^2 = A^2 + B^2.
4. The result is printed with two decimal places using string formatting.

To run the script, save it to a file named `calculator.py`, and then execute the command `python calculator.py` in the terminal.