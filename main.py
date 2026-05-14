import os
import shutil
import logging


# Log file setup
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def scan_folder():

    try:
        folder_path = input("Enter folder path: ")

        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            logging.info("Folder not found")
            return

        items = os.listdir(folder_path)

        if len(items) == 0:
            print("Folder is empty.")
            logging.info("Empty folder scanned")
            return

        print("\nFiles and Folders:\n")

        for item in items:
            print(item)

        logging.info("Folder scanned successfully")

    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")


def organize_files():

    try:
        folder_path = input("Enter folder path: ")

        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            logging.info("Folder not found")
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

                    logging.info(f"Moved file: {item}")

                    break

    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")


def delete_empty_folders():

    try:
        folder_path = input("Enter folder path: ")

        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            logging.info("Folder not found")
            return

        found = False

        for root, dirs, files in os.walk(folder_path, topdown=False):

            for folder in dirs:

                folder_path_full = os.path.join(root, folder)

                if len(os.listdir(folder_path_full)) == 0:

                    os.rmdir(folder_path_full)

                    print(f"Deleted: {folder_path_full}")

                    logging.info(f"Deleted folder: {folder}")

                    found = True

        if not found:
            print("No empty folders found.")

    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")


print("\nPython Automation Script\n")

print("1. Scan Folder")
print("2. Organize Files")
print("3. Delete Empty Folders")
print("4. Exit")

choice = input("\nEnter choice: ")

if choice == "1":
    scan_folder()

elif choice == "2":
    organize_files()

elif choice == "3":
    delete_empty_folders()

elif choice == "4":
    print("Program closed.")

else:
    print("Invalid choice")