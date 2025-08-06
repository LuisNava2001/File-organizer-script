#   A simple and beginner-friendly script written in Python that organizes files in a directory 
#   into categorized folders (e.g., Pictures, Documents, Videos, Music, etc.).
#           Copyright (c) 2025 Luis Nava
#           08/06/2025


import os
import shutil

#   Define the folder to organize
#   Example of target folder
#   target_folder = 'C:/Users/Luis Nava/Downloads'

#   Map extensions to folder names
extension_map = {
    'Pictures': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.aac'],
    "Archives": [".zip", ".rar", ".7z"],
    "Others": []  # fallback
    # Add more categories/extensions if you want
}

def select_option():
    print("#############################################################################################\n")
    print("Welcome to the File Organizer Script!")
    print("This script organizes files into folders like Pictures, Documents, Videos, and more.\n")
    print("Choose an option to continue:")
    print("1. Organize a specific directory (Example: C:/Users/Luis Nava/Downloads)")
    print("2. Organize the current working directory (where this script is located)\n")
    print("#############################################################################################\n")

    while True:
        option = input("Select an option (1 or 2): ").strip()

        if option == "1":
            folder = input("Enter the path of the folder you want to organize: ").strip()
            if not os.path.isdir(folder):
                print("Error!! Invalid Folder. Please check the path and try again...")
                continue
            return folder
        elif option == "2":
            cwd = os.getcwd()
            print(f"Using Current Working Directory: {cwd}")
            return cwd
        else:
            print("Invalid option! Please enter 1 or 2.\n")

def organize_files(folder):
    #   Initialize variables
    num_files = 0
    num_pictures = 0
    num_documents = 0
    num_videos = 0
    num_music = 0
    num_archives = 0
    num_others = 0
    #   Scan all items in the folder
    #   listdir (list of all the documents inside)
    #   join (Function to combine two or more strings into one valid file path)
    #   Example: 'C:/Users/Luis Nava/Downloads/hola.jpeg'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        #   Skip if it is a directory or the main.py
        #   isdir (Returns True if the given path is a directory (folder), and False if it’s a file or doesn't exist)
        if os.path.isdir(file_path) or filename == "main.py":
            continue

        #   Get file extension and make lowercase
        #   splitext (splits a file name into: the name part (before the dot) and the extension (after the dot))
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        #   Determine the folder name for this extension
        destination_folder = None
        #   folder_name takes the list name values from extension_map
        #   extensions take the values of the list from extension_map
        for folder_name, extensions in extension_map.items():
            if ext in extensions:
                destination_folder = folder_name
                if destination_folder == 'Pictures':
                    num_pictures += 1
                elif destination_folder == 'Documents':
                    num_documents += 1
                elif destination_folder == 'Videos':
                    num_videos += 1
                elif destination_folder == 'Music':
                    num_music += 1
                elif destination_folder == 'Archives':
                    num_archives += 1
                break
        
        #   If no matching category, put files in 'Others'
        if destination_folder is None:
            destination_folder = 'Others'
            num_others += 1
        
        #   Create destination folder if it doesn't exist
        dest_path = os.path.join(folder, destination_folder)
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        
        #   Move the file
        shutil.move(file_path, os.path.join(dest_path, filename))
        num_files += 1
        print(f"Moved {filename} to {destination_folder}")
    print("#############################################################################################")
    print(f"Total files moved to Documents: {num_documents}")
    print(f"Total files moved to Pictures: {num_pictures}")
    print(f"Total files moved to Videos: {num_videos}")
    print(f"Total files moved to Music: {num_music}")
    print(f"Total files moved to Archives: {num_archives}")
    print(f"Total files moved to Others: {num_others}")
    print("#############################################################################################")
    print(f"Organized {num_files} files in '{target_folder}'.")
    print("#############################################################################################")

if __name__ == '__main__':
    target_folder = select_option()
    organize_files(target_folder)