Sure! Here is a Python script that accepts a PNG image and deep fries it using the `PIL` library:

```python
from PIL import Image, ImageEnhance

# Function to deep fry the image
def deep_fry_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Increase the saturation
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(2)

    # Increase the contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)

    # Increase the sharpness
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(2)

    # Save the deep fried image
    fried_image_path = image_path.replace('.png', '_fried.png')
    img.save(fried_image_path)
    print(f"Deep fried image saved as {fried_image_path}")

# Ask user for the path of the PNG image
image_path = input("Enter the path of the PNG image: ")

# Deep fry the image
deep_fry_image(image_path)
```

To run this script, save it in a file called `task.py` and then run `python task.py` in the command line. The script will prompt you to enter the path of the PNG image you want to deep fry. Once you provide the path, it will process the image and save the deep fried image as `<original_file_name>_fried.png` in the same directory.

Note: Make sure you have the `PIL` library installed in your Python environment. You can install it using `pip install pillow`.