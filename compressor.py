from PIL import Image
import os

def compress_images(directory, quality):
    # Get all files in the specified directory
    files = os.listdir(directory)
    
    for file in files:
        if file.endswith('.JPG') or file.endswith('.jpeg'):
            file_path = os.path.join(directory, file)
            # Open an image file
            with Image.open(file_path) as img:
                # Save the image with reduced quality but same dimensions
                img.save(file_path, quality=quality)
                print(f"{file} compressed successfully!")

# Replace with the directory containing your images
directory = "assets/img/gallery"
# Quality parameter, it can range from 0 (worst) to 100 (best), usually, 85 is a good compromise
quality = 85
compress_images(directory, quality)
