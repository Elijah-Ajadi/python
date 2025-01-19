import os
import shutil
## A simple script to organize files in my Downloads folder


downloads_folder = os.path.expanduser("~/Downloads")
organization_map = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv", ".php"],
    "Zips": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso", ".tar.xz"],
    "Audio": [".mp3"],
	
}

def create_folders():
    for folder_name in organization_map.keys():
        folder_path = os.path.join(downloads_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files():
    for item in os.listdir(downloads_folder):
        item_path = os.path.join(downloads_folder, item)

        if os.path.isdir(item_path):
            continue

        _, file_extension = os.path.splitext(item)

        for folder_name, extensions in organization_map.items():
            if file_extension.lower() in extensions:
                destination_folder = os.path.join(downloads_folder, folder_name)
                shutil.move(item_path, destination_folder)
                print(f"Moved: {item} -> {folder_name}")
                break

if __name__ == "__main__":
    create_folders()
    organize_files()
    print("Downloads folder organized successfully!")
