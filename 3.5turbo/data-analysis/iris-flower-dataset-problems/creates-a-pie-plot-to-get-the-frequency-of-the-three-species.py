Sure! Here's the Python code that creates a pie plot to display the frequency of the three species in the Iris dataset:

```python
import pandas as pd
import matplotlib.pyplot as plt

def create_pie_plot():
    # Load the Iris dataset
    df = pd.read_csv('iris.csv')

    # Count the frequency of each species
    species_counts = df['species'].value_counts()

    # Create a pie plot
    plt.figure(figsize=(8, 6))
    plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle
    plt.title('Frequency of Species in Iris Dataset')
    plt.show()

if __name__ == '__main__':
    create_pie_plot()
```

In the above code:

1. We first import the necessary libraries: pandas for data loading and manipulation, and matplotlib.pyplot for plotting.
2. The `create_pie_plot` function is defined to encapsulate the plot creation code.
3. Inside the function, we load the Iris dataset using `pd.read_csv` and store it in a DataFrame called `df`.
4. We then count the frequency of each species using `value_counts` on the 'species' column of the DataFrame and store it in the `species_counts` variable.
5. Next, we create the pie plot using `plt.pie`. We pass `species_counts` as the data to be plotted, `labels=species_counts.index` to set the labels as species names, `autopct='%1.1f%%'` to display the percentage values on the pie slices, and `startangle=90` to rotate the plot by 90 degrees.
6. We set `plt.axis('equal')` to ensure the pie plot is drawn as a circle.
7. Finally, we set the plot title using `plt.title` and display the plot using `plt.show`.
8. The `if __name__ == '__main__'` line ensures that the `create_pie_plot` function is only called if the script is run directly.

To run the script, save the code in a file named `task.py` in the same directory as your 'iris.csv' dataset file. Then, open a terminal or command prompt in that directory and run `python task.py`. The pie plot will be displayed.