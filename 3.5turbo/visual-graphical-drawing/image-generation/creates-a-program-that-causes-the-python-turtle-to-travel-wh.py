Sure! Here's a Python script that uses the `turtle` library to create a program that allows the turtle to travel wherever the mouse gets clicked on the screen and leave a trail:

```python
import turtle

def move_to(x, y):
    turtle.goto(x, y)  # Move turtle to the clicked position
    turtle.stamp()  # Leave a stamp at the position

def main():
    turtle.speed(0)  # Set the turtle's speed to the fastest

    turtle.onscreenclick(move_to)  # Call move_to function when the mouse is clicked

    turtle.mainloop()  # Start the turtle's main loop

if __name__ == "__main__":
    main()
```

To run the program, save the code in a file named `task.py` and execute it using the command `python task.py` in the terminal.

The `move_to` function is called whenever the mouse is clicked on the screen. It moves the turtle to the clicked position using the `goto` method and leaves a stamp at that position using the `stamp` method.

The `main` function sets the turtle's speed to the fastest, registers the `move_to` function to be called when the mouse is clicked using the `onscreenclick` method, and starts the turtle's main loop using the `mainloop` method.

Please make sure to have the `turtle` library installed before running the script. You can install it by running `pip install PythonTurtle`.