Here is a Python script that takes an equation and solves for x:

```python
import sympy

def solve_equation(equation):
    x = sympy.symbols('x')
    equation = sympy.sympify(equation)
    solution = sympy.solve(equation, x)
    return solution

if __name__ == "__main__":
    equation = input("Enter an equation: ")
    solution = solve_equation(equation)
    print("Solution for x:")
    print(solution)
```

This script uses the `sympy` library, which is a powerful symbolic math library in Python. It allows us to define symbols and equations, and solve them symbolically.

In the `solve_equation` function, we first define the symbol `x` using `sympy.symbols`. We then convert the input equation into a symbolic expression using `sympy.sympify`. Finally, we use `sympy.solve` to solve the equation and obtain the solution for `x`.

In the `main` section of the script, we ask the user to input an equation, and then call the `solve_equation` function to solve it. The resulting solution is then printed to the console.

To run this script, save it to a file called `task.py` and run `python task.py` in the command line.