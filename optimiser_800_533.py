from PIL import Image, ImageSequence
import os

def resize_gif(image_path, output_path, size=(800, 533)):
    img = Image.open(image_path)
    frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
    resized_frames = []

    for frame in frames:
        new_frame = frame.resize(size, Image.ANTIALIAS)
        resized_frames.append(new_frame)

    resized_frames[0].save(output_path, save_all=True, append_images=resized_frames[1:])

def crop_and_resize(image_path, output_path, size=(800, 533)):
    if image_path.lower().endswith('.gif'):
        resize_gif(image_path, output_path, size)
        return

    img = Image.open(image_path)
    img_resized = img.resize(size, Image.ANTIALIAS)
    img_resized.save(output_path)

image_directory = "assets/img/demos"  
output_directory = os.path.join(image_directory, "trial")

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

all_files = os.listdir(image_directory)
image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    output_path = os.path.join(output_directory, f"optimised_{image_file}")
    crop_and_resize(image_path, output_path)
