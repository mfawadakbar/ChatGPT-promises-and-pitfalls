from PIL import Image
import glob, os


def flip_image(IMG_PATH, FLIP_TYPE):
    # Open the image file
    image = Image.open(IMG_PATH)

    # Flip the image vertically
    if FLIP_TYPE == "vertical":
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    # Flip the image horizontally
    elif FLIP_TYPE == "horizontal":
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        return "Invalid flip type. Please choose 'vertical' or 'horizontal'."

    # Save the flipped image
    flipped_image.save(
        "flipped_image.png"
    )  # You can change the output file name if needed
    return "Image flipped successfully."


if __name__ == "__main__":
    # Ask for user input
    print("Current Working Directory: ", os.getcwd())
    IMG_PATH = input("Enter the path to the image file: ")
    IMG_PATH = glob.glob(IMG_PATH)
    FLIP_TYPE = input("Enter the flip type (vertical/horizontal): ")

    if IMG_PATH[-4:] not in [".png", ".jpg", ".gif"]:
        raise Exception("Image is not a png, jpg, or gif")
    else:
        print(f"Flipping image... {IMG_PATH}")
        # Flip the image and display the result
        print(flip_image(IMG_PATH, FLIP_TYPE))
