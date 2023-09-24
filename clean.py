import os
import re

# Define the directory path
directory_path = r'C:\Marcus\Important Docs\MLSA\WikiArt'

# List of words to remove from filenames
words_to_remove = ["train", "test", "valid"]

# Function to rename files
def rename_files(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            # Use regular expressions to replace "train," "test," and "valid" in filenames
            new_filename = re.sub(r'(?i)(train|test|valid)', '', filename)
            
            # Check if the filename has changed
            if new_filename != filename:
                old_path = os.path.join(foldername, filename)
                new_path = os.path.join(foldername, new_filename)
                # Rename the file
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} -> {new_filename}')

# Call the function to rename files
rename_files(directory_path)
