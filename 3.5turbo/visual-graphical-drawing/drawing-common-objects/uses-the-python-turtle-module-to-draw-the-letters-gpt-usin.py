Sure! Here is a Python script that uses the turtle module to draw the letters "GPT" using only lines:

```python
import turtle

def draw_G():
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)

def draw_P():
    turtle.up()
    turtle.goto(50, 0)
    turtle.down()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)

def draw_T():
    turtle.up()
    turtle.goto(200, 0)
    turtle.down()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)

if __name__ == "__main__":
    turtle.speed(2)  # Speed of drawing
    draw_G()
    draw_P()
    draw_T()
    turtle.done()
```

Save the above code in a file called `task.py`, and you can run it using the command `python task.py`. The script will draw the letters "GPT" using lines using the turtle module.