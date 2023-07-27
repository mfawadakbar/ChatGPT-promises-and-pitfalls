Certainly! Here's a Python script that accepts an image file in PNG, JPEG, or GIF format, and flips it vertically or horizontally based on user input.

```python
from PIL import Image

def flip_image(image_path, flip_type):
    # Open the image file
    image = Image.open(image_path)
    
    # Flip the image vertically
    if flip_type == 'vertical':
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    # Flip the image horizontally
    elif flip_type == 'horizontal':
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        return "Invalid flip type. Please choose 'vertical' or 'horizontal'."
    
    # Save the flipped image
    flipped_image.save("flipped_image.png")  # You can change the output file name if needed
    return "Image flipped successfully."

# Ask for user input
image_path = input("Enter the path to the image file: ")
flip_type = input("Enter the flip type (vertical/horizontal): ")

# Flip the image and display the result
print(flip_image(image_path, flip_type))
```

To run this script, save it in a file named `image_flip.py` and execute it using the command `python image_flip.py`. The script will prompt you to enter the path to the image file and the flip type (vertical or horizontal). After the image is flipped, it will be saved as `flipped_image.png` in the same directory.