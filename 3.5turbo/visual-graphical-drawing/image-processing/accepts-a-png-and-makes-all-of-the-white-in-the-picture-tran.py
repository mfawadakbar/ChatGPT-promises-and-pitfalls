Here's a Python script that accepts a PNG image and makes all of the white pixels transparent. It uses the Pillow library to process the image.

```python
from PIL import Image

def make_white_pixels_transparent(image_path):
    # Open the image using Pillow
    img = Image.open(image_path)

    # Convert the image to RGBA mode (if not already)
    img = img.convert("RGBA")

    # Get the image data as a list of pixels
    pixel_data = img.getdata()

    # Loop through each pixel
    new_pixel_data = []
    for item in pixel_data:
        # If the pixel is white, make it transparent
        if item[:3] == (255, 255, 255):
            new_pixel_data.append((255, 255, 255, 0))
        else:
            new_pixel_data.append(item)

    # Update the image data
    img.putdata(new_pixel_data)

    # Save the modified image
    img.save("transparent_image.png")

if __name__ == "__main__":
    # Prompt the user for the image file path
    image_path = input("Enter the path to the PNG image: ")

    # Call the function to make white pixels transparent
    make_white_pixels_transparent(image_path)
```

To use this script, save the code into a file named `task.py`, and then run it with the command `python task.py`. The script will prompt you to enter the path to the PNG image you want to process. After running, it will create a new PNG file named `transparent_image.png` with all the white pixels made transparent.