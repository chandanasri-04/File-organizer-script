import os
import shutil
import logging
from datetime import datetime

# ========== CONFIG ==========
SOURCE_FOLDER = r"D:\internship (python)\New folder"  
DRY_RUN = False  # True = preview only, False = actually move files
LOG_FILE = "file_organizer.log"

# ========== SETUP LOGGING ==========
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ========== FUNCTION ==========
def organize_files(folder):
    if not os.path.exists(folder):
        print("Folder does not exist!")
        return

    print(f"\nScanning folder: {folder}\n")

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        ext = file.split('.')[-1].lower()

        # Handle files without extension
        if '.' not in file:
            ext = "no_extension"

        # Create subfolder
        target_folder = os.path.join(folder, ext)
        os.makedirs(target_folder, exist_ok=True)

        # Handle name collision
        new_file_path = os.path.join(target_folder, file)
        base, extension = os.path.splitext(file)
        counter = 1

        while os.path.exists(new_file_path):
            new_name = f"{base}_{counter}{extension}"
            new_file_path = os.path.join(target_folder, new_name)
            counter += 1

        # Move or Dry Run
        if DRY_RUN:
            print(f"[DRY RUN] Would move: {file} -> {target_folder}")
        else:
            shutil.move(file_path, new_file_path)
            print(f"Moved: {file} -> {target_folder}")
            logging.info(f"Moved: {file} -> {target_folder}")

# ========== RUN ==========
if __name__ == "__main__":
    organize_files(SOURCE_FOLDER)