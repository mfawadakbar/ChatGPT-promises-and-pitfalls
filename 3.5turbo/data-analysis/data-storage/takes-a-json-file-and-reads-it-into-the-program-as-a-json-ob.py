Here's a Python script that reads a JSON file and loads it into a JSON object:

```python
import json

def read_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data

def main():
    # Prompt the user for the JSON file path
    file_path = input("Enter the path to the JSON file: ")
    
    try:
        # Read the JSON file into a JSON object
        json_data = read_json_file(file_path)
        
        # Process the JSON data as needed
        # ...
        
        print("JSON file loaded successfully!")
    except FileNotFoundError:
        print("File not found!")
    except json.JSONDecodeError:
        print("Invalid JSON format!")

if __name__ == '__main__':
    main()
```

To use this script, save it in a file named `task.py` and run it using the command `python task.py`. The script will prompt you to enter the path to the JSON file, and then it will load the file as a JSON object using the `json.load()` method. You can then process the JSON data as needed within the `try` block.

Note: This script assumes that the JSON file exists and is in a valid JSON format. You can add additional error handling and validation as required.