import os
import shutil

def group_files_by_keyword(keyword, source_directory, destination_directory):
    # Normalize keyword and destination folder name
    keyword = keyword.lower()
    destination_folder = os.path.join(destination_directory, keyword.capitalize())
    
    # Create the destination folder if it does not exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all files in the source directory
    for filename in os.listdir(source_directory):
        # Check if the keyword is in the filename (case insensitive)
        if keyword in filename.lower():
            # Move the file to the destination folder
            shutil.move(os.path.join(source_directory, filename), destination_folder)
            print(f'Moved file: {filename} to folder: {destination_folder}')

# Usage
# Define the input keyword, source, and destination directories
input_keyword = "mytype"  # Example input
source_dir = "/path/to/source_directory"  # Path where the files are located
destination_dir = "/path/to/destination_directory"  # Path where files should be moved

# Run the function
group_files_by_keyword(input_keyword, source_dir, destination_dir)
