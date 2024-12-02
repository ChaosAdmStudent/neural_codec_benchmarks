import os

def rename_files_to_dcvc_format(directory):
    """
    Renames files in the specified directory to follow DCVC naming conventions (im00001.png, im00002.png, etc.).
    Assumes files are named with a numeric suffix, e.g., test_0.png, test_1.png, etc.
    """
    # Read all files in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.png')]
    
    # Extract numeric part and sort files
    sorted_files = sorted(files, key=lambda x: int(''.join(filter(str.isdigit, x))))
    
    # Rename files to DCVC convention
    for idx, filename in enumerate(sorted_files, start=1):
        new_name = f"im{idx:05d}.png"  # Format: im00001.png, im00002.png, etc.
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

# Specify your directory path
directory_path = "/w/331/lgupta/DCVC/DCVC/media/data/vcd/video_5"  # Update this path to your dataset directory

# Call the function
rename_files_to_dcvc_format(directory_path)