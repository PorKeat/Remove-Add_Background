from PIL import Image
import os

input_folder = r'D:\Python\Testing\removeTheara'
output_folder = r'D:\Python\Testing\imageTheara'

target_size = (241, 201)

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGBA")

        img.thumbnail(target_size, Image.Resampling.LANCZOS)

        background = Image.new('RGBA', target_size, (255, 255, 255, 255))

        img_position = (
            (target_size[0] - img.width) // 2,
            (target_size[1] - img.height) // 2
        )
        background.paste(img, img_position, img)

        final_img = background.convert('RGB')

        base_name = os.path.splitext(filename)[0]
        save_path = os.path.join(output_folder, base_name + '.jpg')
        final_img.save(save_path, format='JPEG', quality=95)

        print(f"Processed: {filename} → Saved as {base_name}.jpg")

print("✅ Successfully")
