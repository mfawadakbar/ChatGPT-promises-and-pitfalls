```python
import turtle

# Constants for the size of each square on the chessboard
SQUARE_SIZE = 50
BOARD_SIZE = 8

def draw_chessboard():
    # Set up the turtle
    screen = turtle.Screen()
    screen.title("Chessboard")
    turtle.setup(BOARD_SIZE * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE)
    turtle.penup()
    
    # Start drawing the chessboard
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Determine the position of the current square
            x = col * SQUARE_SIZE - (BOARD_SIZE * SQUARE_SIZE) / 2
            y = row * SQUARE_SIZE - (BOARD_SIZE * SQUARE_SIZE) / 2
            
            # Move the turtle to the current square's position
            turtle.goto(x, y)
            
            # Determine the color of the current square
            if (row + col) % 2 == 0:
                color = "white"
            else:
                color = "black"
            
            # Draw the current square
            turtle.fillcolor(color)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(SQUARE_SIZE)
                turtle.right(90)
            turtle.end_fill()

    # Hide the turtle
    turtle.hideturtle()

    # Keep the turtle window open until it is closed
    turtle.done()

# Call the function to draw the chessboard
draw_chessboard()
```

This script uses the turtle module to draw a 2D 8x8 chessboard with alternating black and white squares. It sets up the turtle, loops through each square on the chessboard, determines its position and color, and uses the turtle to draw the square. It then hides the turtle and keeps the turtle window open until it is closed.