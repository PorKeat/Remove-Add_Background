import os
from rembg import remove

def remove_background(input_image_path, output_image_path):
    with open(input_image_path, 'rb') as input_file:
        input_image = input_file.read()
    output_image = remove(input_image)
    with open(output_image_path, 'wb') as output_file:
        output_file.write(output_image)
    print(f"Background removed: {input_image_path} -> {output_image_path}")

def process_images_in_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        input_image_path = os.path.join(input_folder, filename)
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            output_image_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
            remove_background(input_image_path, output_image_path)

input_folder = r'D:\thearaImg'
output_folder = r'D:\Python\Testing\removeTheara'
os.makedirs(output_folder, exist_ok=True)
process_images_in_folder(input_folder, output_folder)
