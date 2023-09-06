#100daysofcode
import os

image_folder = "exercise_7/"

if not os.path.exists(image_folder):
    print("Folder not found.")
else:
    print("Folder found:", image_folder)
    i = 0
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(".png"):
            i += 1
            new_filename = f"image_{i}.png"
            old_path = os.path.join(image_folder, filename)
            new_path = os.path.join(image_folder, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")
