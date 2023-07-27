Sure! Here's a Python script that takes a dataset and vectorizes the text using the scikit-learn library:

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
dataset = pd.read_csv('dataset.csv')

# Extract the text data
text_data = dataset['text']

# Initialize the vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the text data
vectorized_data = vectorizer.fit_transform(text_data)

# Print the vectorized data
print(vectorized_data)
```

You need to have the `pandas` and `scikit-learn` libraries installed to run this script. Please make sure the dataset is in a CSV file named `dataset.csv` and has a column named `text` that contains the text data.

To run the script, save it to a file named `task.py` and execute the command `python task.py` in your terminal.

Let me know if you need any further assistance!