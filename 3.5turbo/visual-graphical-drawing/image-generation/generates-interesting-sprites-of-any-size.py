import random
from PIL import Image

def generate_sprite(width, height):
    sprite = Image.new('RGB', (width, height))

    # Define random colors for the sprite
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Generate interesting patterns for the sprite
    for y in range(height):
        for x in range(width):
            if (x + y) % 2 == 0:
                sprite.putpixel((x, y), color1)
            else:
                sprite.putpixel((x, y), color2)

    return sprite

def save_sprite(sprite, name):
    sprite.save(name)

# Ask user for the size of the sprite
width = int(input("Enter the width of the sprite: "))
height = int(input("Enter the height of the sprite: "))

# Generate and save the sprite
sprite = generate_sprite(width, height)
save_sprite(sprite, "sprite.png")