import os
import shutil

# Define the directory path, defaults to the current directory
dir_path = os.getcwd()

# Supported folder to be sorted into
TEXT_FILE = "TextFiles"
PDFs  = "PDFs"
DOCX = "WordDocs"
EXCEL = "ExcelDocs"
IMAGES = "Images"
MUSIC = "Music"
VIDOES = "Videos"
EXE = "Executables"
BIN = "Binaries"

# Create a dictionary to store file extensions and their corresponding directories
file_extensions = {
    'txt': TEXT_FILE,
    'pdf': PDFs,
    'docx': DOCX,
    'xlsx': EXCEL,
    'jpg': IMAGES,
    'png': IMAGES,
    'mp3': MUSIC,
    'mp4': VIDOES,
    'bin': BIN,
    'exe': EXE,
}


def main(dir_path=dir_path):
    # Loop through each file in the directory
    for filename in os.listdir(dir_path):
        # Get the file extension
        extension = os.path.splitext(filename)[1][1:].lower()
        
        # Check if the file has an extension and if it's in the dictionary
        if extension and extension in file_extensions:
            # Get the corresponding directory for the file extension
            sub_dir = os.path.join(dir_path, file_extensions[extension])
            
            # If the directory doesn't exist, create it
            if not os.path.exists(sub_dir):
                os.mkdir(sub_dir)
            
            # Move the file to the corresponding directory
            shutil.move(os.path.join(dir_path, filename), os.path.join(sub_dir, filename))
            
    print("Files have been sorted and arranged successfully!")


if __name__ == "__main__":
    main()