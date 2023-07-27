Sure! Here's an example of how you can build a predictive model using the scikit-learn library and the Boston Housing dataset:

```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the Boston Housing dataset
boston = load_boston()
data = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
```

This script loads the Boston Housing dataset using the `load_boston` function from scikit-learn. We then split the dataset into training and test sets using `train_test_split`. Next, we create a linear regression model using `LinearRegression` and train it on the training set. We then make predictions on the test set using the `predict` method. Finally, we evaluate the model using the mean squared error metric and print the result.

To run this script, save it as `task.py` and execute it using the command `python task.py`.