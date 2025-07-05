import os
import shutil

# Paths (CHANGE THESE)
image_folder = r'D:\projects\drowsiness_detection\dataset\images\val\new_val'         # Folder with images
label_folder = r'D:\projects\drowsiness_detection\dataset\labels'         # Folder with .txt annotations
output_folder = r'D:\projects\drowsiness_detection\dataset\val\new_val' # Folder to copy matched .txt files

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get image names without extension
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
image_names = [os.path.splitext(f)[0] for f in image_files]

# Match, copy, and delete .txt files
matched = 0
for name in image_names:
    txt_filename = name + '.txt'
    txt_path = os.path.join(label_folder, txt_filename)
    if os.path.exists(txt_path):
        shutil.copy(txt_path, os.path.join(output_folder, txt_filename))  # Copy
        os.remove(txt_path)  # Delete original
        matched += 1

print(f"✅ {matched} annotation files copied to '{output_folder}' and removed from '{label_folder}'.")
