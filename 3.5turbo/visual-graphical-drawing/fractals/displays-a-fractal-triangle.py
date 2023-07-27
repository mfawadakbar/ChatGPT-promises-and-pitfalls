Sure, here's a Python script that displays a Fractal Triangle using the turtle module:

```python
import turtle

def draw_fractal(length, depth):
    if depth == 0:
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
    else:
        draw_fractal(length / 2, depth - 1)
        turtle.forward(length / 2)
        draw_fractal(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        draw_fractal(length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

def main():
    turtle.speed(0)  # Set the turtle speed to the maximum
    length = 200     # Length of the initial triangle side
    depth = 4        # Recursive depth (increase for more detail)
    
    draw_fractal(length, depth)
    turtle.done()

if __name__ == "__main__":
    main()
```

To run the script, save it in a file called "fractal_triangle.py", then execute it by running the command "python fractal_triangle.py" in the terminal. The turtle graphics window will appear, and you will see the fractal triangle being drawn.

You can adjust the `length` and `depth` variables in the `main` function to create different sizes and levels of detail for the fractal triangle. The turtle's speed is set to 0 to draw instantly, but you can modify it to a lower value if you want to see the drawing process.