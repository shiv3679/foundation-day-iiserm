from PIL import Image
import os

def crop_and_resize_to_square(image_path, output_path, size=(600, 600)):
    # Open an image file
    img = Image.open(image_path)
    width, height = img.size

    # Find dimensions for cropping to a square
    new_dimension = min(width, height)
    left = (width - new_dimension) / 2
    top = (height - new_dimension) / 2
    right = (width + new_dimension) / 2
    bottom = (height + new_dimension) / 2

    # Crop the image
    img_cropped = img.crop((left, top, right, bottom))

    # Resize the image
    img_resized = img_cropped.resize(size, Image.ANTIALIAS)

    # Save the image
    img_resized.save(output_path)

# Directory where images are stored
image_directory = "assets/img/coordinators"  # Replace with the path to your image folder

# Directory to save cropped images
output_directory = os.path.join(image_directory, "optimised")

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all files in the directory
all_files = os.listdir(image_directory)

# Filter out image files
image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Crop and resize each image in the list
for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    output_path = os.path.join(output_directory, f"optimised_{image_file}")
    crop_and_resize_to_square(image_path, output_path)

# The script will crop and resize all the images in the folder to 600x600 pixels 
# and save them in the "optimised" folder. Images will be overwritten if they already exist.
