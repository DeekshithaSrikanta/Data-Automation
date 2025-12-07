import os
import shutil

def organize_files(folder):
    # Define file categories
    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Apps": [".exe", ".msi", ".apk"],
        "Music": [".mp3", ".wav"]
    }

    # List all files
    files = os.listdir(folder)

    for file in files:
        file_path = os.path.join(folder, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(file)[1].lower()
        moved = False

        # Check each category
        for category, ext_list in extensions.items():
            if ext in ext_list:
                category_folder = os.path.join(folder, category)
                os.makedirs(category_folder, exist_ok=True)
                
                shutil.move(file_path, os.path.join(category_folder, file))
                moved = True
                break

        # If file doesn't match any known extension
        if not moved:
            others_folder = os.path.join(folder, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, file))

    print("✅ Files organized successfully!")

# ---------------- MAIN ----------------
print("\n--- File Organizer ---")
path = input("Enter folder path to organize: ")

if os.path.exists(path):
    organize_files(path)
else:
    print("❌ Invalid path!")