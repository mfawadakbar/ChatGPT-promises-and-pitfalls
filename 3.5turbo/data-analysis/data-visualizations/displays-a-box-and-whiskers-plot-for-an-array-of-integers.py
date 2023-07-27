Sure! Here's an example of a Python script that uses the `matplotlib` library to create a box and whiskers plot for an array of integers:

```python
import matplotlib.pyplot as plt
import numpy as np

def create_boxplot(data):
    fig, ax = plt.subplots()
    ax.boxplot(data)

    ax.set_xlabel('Data')
    ax.set_ylabel('Values')
    ax.set_title('Box and Whiskers Plot')

    plt.show()

if __name__ == '__main__':
    # Example input: array of integers
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    create_boxplot(data)
```

In this script, we define a function `create_boxplot` that takes an array of integers as input. Inside the function, we use the `boxplot()` function from `matplotlib` to create the box and whiskers plot. We then set the labels and title for the plot using the `set_xlabel()`, `set_ylabel()`, and `set_title()` functions.

Finally, in the `if __name__ == '__main__':` block, we create an example input array of integers and call the `create_boxplot` function to generate the plot.

To run this script, save it in a file called `task.py` and run `python task.py` in your command prompt or terminal.