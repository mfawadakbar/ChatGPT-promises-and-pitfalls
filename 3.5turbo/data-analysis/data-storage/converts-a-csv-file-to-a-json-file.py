Here's the Python code to convert a CSV file to a JSON file:

```python
import csv
import json

def convert_csv_to_json(csv_file, json_file):
    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # Write the JSON file
    with open(json_file, 'w') as file:
        json.dump(rows, file, indent=4)

# Run the conversion
csv_file = 'input.csv'
json_file = 'output.json'
convert_csv_to_json(csv_file, json_file)
```

To use this code:

1. Save the above code in a file called "task.py".
2. Place your CSV file in the same directory as "task.py".
3. Replace `input.csv` with the actual name of your CSV file.
4. Replace `output.json` with the desired name of your JSON output file.
5. Run the script using the command `python task.py`.

The CSV file will be converted to a JSON file with the same data.