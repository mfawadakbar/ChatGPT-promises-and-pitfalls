Sure! Here's a Python script that creates and displays a discrete graph using the matplotlib library:

```python
import matplotlib.pyplot as plt

def create_discrete_graph():
    # Define x and y values for the graph
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the discrete graph
    ax.plot(x, y, marker='o')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Discrete Graph')

    # Show the graph
    plt.show()

if __name__ == "__main__":
    # Call the function to create and display the graph
    create_discrete_graph()
```

To run this script, save it as `task.py` and execute the command `python task.py` in your terminal. It will display a simple discrete graph with x and y coordinates specified in the code.

You can customize the x and y values to create different discrete graphs. You can also explore more options and features provided by the matplotlib library to enhance the graph as per your requirements.