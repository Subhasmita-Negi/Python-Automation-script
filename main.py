import os
import shutil



def scan_folder():

    try:
        folder_path = input("Enter folder path: ")

        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            return

        items = os.listdir(folder_path)

        if len(items) == 0:
            print("Folder is empty.")
            return

        print("\nFiles and Folders:\n")

        for item in items:
            print(item)

    except Exception as e:
        print(f"Error: {e}")



def organize_files():

    try:
        folder_path = input("Enter folder path: ")

        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            return

        file_types = {
            "Images": [".jpg", ".png", ".jpeg"],
            "Documents": [".pdf", ".txt", ".docx"],
            "Music": [".mp3"],
            "Videos": [".mp4"]
        }

        items = os.listdir(folder_path)

        for item in items:

            item_path = os.path.join(folder_path, item)

            # Skip folders
            if os.path.isdir(item_path):
                continue

            _, extension = os.path.splitext(item)

            for folder_name, extensions in file_types.items():

                if extension.lower() in extensions:

                    target_folder = os.path.join(folder_path, folder_name)

                    os.makedirs(target_folder, exist_ok=True)

                    shutil.move(
                        item_path,
                        os.path.join(target_folder, item)
                    )

                    print(f"Moved: {item} -> {folder_name}")

                    break

    except Exception as e:
        print(f"Error: {e}")



print("1. Scan Folder")
print("2. Organize Files")

choice = input("Enter choice: ")

if choice == "1":
    scan_folder()

elif choice == "2":
    organize_files()

else:
    print("Invalid choice")