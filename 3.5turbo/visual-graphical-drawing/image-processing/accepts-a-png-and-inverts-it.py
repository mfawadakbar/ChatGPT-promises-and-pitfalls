Sure! Here's a Python script that accepts a PNG file and inverts its colors using the pillow library:

```python
from PIL import Image

def invert_image(image_path):
    # Open the image using PIL
    image = Image.open(image_path)

    # Invert the image
    inverted_image = Image.eval(image, lambda x: 255 - x)

    # Save the inverted image
    inverted_image.save("inverted.png")
    print("Image inverted and saved as inverted.png")


# Prompt the user for the image file path
image_path = input("Enter the path to the PNG image: ")

# Call the invert_image function with the provided path
invert_image(image_path)
```

To run the script, save it to a file named `task.py`, make sure you have the pillow library installed (`pip install pillow`), and then run `python task.py` in the terminal. The script will prompt you to enter the path to the PNG image file, and after the inversion is done, it will save the inverted image as `inverted.png` in the same directory.

Note: Make sure the image file path is correct and the image format is PNG for this code to work properly.