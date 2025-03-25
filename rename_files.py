import os
import random
import string

def generate_random_name(length=16):
    """
    Generates a random string of Latin letters (A-Z) and digits (0-9) with a given length.
    Length is set to 16 characters by default for a balance between uniqueness and readability.
    """
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

def rename_files(directory):
    """
    Renames all files in the given directory (and its subdirectories) to random names.
    Keeps the original file extension intact.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1]  # Get the file extension
            random_name = generate_random_name() + file_extension  # Add extension back
            new_path = os.path.join(root, random_name)

            # Rename the file
            try:
                os.rename(file_path, new_path)
                print(f"Renamed: {file_path} -> {new_path}")
            except Exception as e:
                print(f"Error renaming {file_path}: {e}")

if __name__ == "__main__":
    # Directory to rename files in (user can customize this)
    target_directory = input("Enter the directory path to rename files: ").strip()
    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        rename_files(target_directory)
        print("All files renamed successfully.")
    else:
        print("Invalid directory path.")
