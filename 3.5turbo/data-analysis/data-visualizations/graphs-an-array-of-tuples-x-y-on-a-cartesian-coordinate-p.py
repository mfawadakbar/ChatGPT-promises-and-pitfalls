Sure! Here's an example of a Python script that uses Matplotlib library to graph an array of tuples (x, y) on a cartesian coordinate plane:

```python
import matplotlib.pyplot as plt

def plot_coordinates(coordinates):
    # Unpack the coordinates array into separate lists of x and y values
    x_values, y_values = zip(*coordinates)

    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Plot the points on the cartesian coordinate plane
    ax.scatter(x_values, y_values)

    # Add labels and a title to the plot
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Plotting Coordinates')

    # Adjust the axis limits to fit the data
    ax.autoscale()

    # Display the plot
    plt.show()

# Test the function with sample coordinates
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
plot_coordinates(coordinates)
```

In this script, the `plot_coordinates` function takes an array of tuples as input. It uses the `zip` function to separate the tuples into separate lists of x and y values. Then, it creates a new figure and axis using `plt.subplots()`. The `scatter` function is used to plot the points on the cartesian coordinate plane. Additional labels and a title are added to the plot using the `set_xlabel`, `set_ylabel`, and `set_title` functions. Finally, the plot is displayed using `plt.show()`.

To run this script, save it to a file named `task.py`, then execute the command `python task.py` in the terminal. The script will plot the sample coordinates provided in the example. Feel free to modify the coordinates array to plot your own set of points.