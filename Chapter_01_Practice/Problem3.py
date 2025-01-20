# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

#  This Code is copied from an AI because with Python 
# I'm learning, How can i sufficently use AI in my Programming Career v
# Becauses It's Now totally AI Generation need enough Knowledge about AI
# To Survive in this Compitative World  

import os

def list_directory_contents(path):
    try:
        # Get the list of all files and directories
        directory_contents = os.listdir(path)
        
        print(f"Contents of '{path}':")
        for item in directory_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"The path '{path}' is not a directory.")
    except PermissionError:
        print(f"Permission denied for accessing '{path}'.")

# Provide the path to the directory you want to list
directory_path = '/'  # Change this to your desired directory path
list_directory_contents(directory_path)
