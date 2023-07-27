Sure, here's an example of a Python script that reads a csv file, extracts the specified headers, and displays a histogram using the matplotlib library:

```python
import pandas as pd
import matplotlib.pyplot as plt

def display_histogram(csv_file, headers):
    # Read the csv file into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    # Select the specified headers from the DataFrame
    selected_columns = df[headers]

    # Create a histogram for each selected column
    selected_columns.hist()

    # Display the histogram
    plt.show()

if __name__ == "__main__":
    # Specify the csv file path
    csv_file = "data.csv"

    # Specify the headers for which the histogram is to be displayed
    headers = ["header1", "header2", "header3"]

    # Call the function to display the histogram
    display_histogram(csv_file, headers)
```

In this script, you'll need to replace `"data.csv"` with the path to your actual csv file, and update `["header1", "header2", "header3"]` with the actual headers you want to display the histogram for.

You'll also need to make sure you have the pandas and matplotlib libraries installed. You can install them using pip:

```
pip install pandas matplotlib
```

Once you've saved the script to a file, you can run it using the command `python task.py`.