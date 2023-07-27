Sure! Here's a python script that uses the SymPy library to calculate the integral of an equation:

```python
import sympy as sp

def calculate_integral():
    # Get the equation from the user
    equation = input("Enter an equation to calculate the integral: ")

    # Create a symbol for the variable used in the equation
    x = sp.symbols('x')

    try:
        # Parse the equation and calculate the integral
        integral = sp.integrate(equation, x)
        return integral
    
    except Exception as e:
        print("Error: ", e)
        return None

# Call the function to calculate the integral
result = calculate_integral()

# Print the result
if result:
    print("The integral is:", result)
else:
    print("Failed to calculate the integral.")
```

To run this script, save it to a file named `task.py` and run it using the command `python task.py`. The script will ask you to enter an equation, and it will calculate the integral of that equation using the sympy library. The result will be printed on the console.

Note that you need to have the sympy library installed in order to run this script. You can install it using the command `pip install sympy`.