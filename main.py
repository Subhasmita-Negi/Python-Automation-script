import os

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



scan_folder()