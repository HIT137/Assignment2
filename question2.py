from PIL import Image
import numpy as np
import time


original_image_path = "/Users/admin/Desktop/chapter1.jpg"
original_image = Image.open(original_image_path)


current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print(generated_number)

original_array = np.array(original_image)
modified_array = np.clip(original_array + generated_number, 0, 255).astype(np.uint8)
modified_image = Image.fromarray(modified_array)

modified_image_path = "/Users/admin/Desktop/chapter1out.jpg"
modified_image.save(modified_image_path)

print("New image with modified pixels saved as 'chapter1out.png' on the desktop.")

red_sum = np.sum(modified_array[:, :, 0])
print("Sum of red pixel values in the modified image:", red_sum)
