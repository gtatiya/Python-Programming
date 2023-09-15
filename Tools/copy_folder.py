import os
import shutil
import distutils.dir_util

'''
Python code that crawls through a given path, and copies any folder with a given name to an given output path with the same relative path.
'''

def copy_folders_by_name(source_dir, destination_dir, folder_name):
    for root, dirs, files in os.walk(source_dir):
        for dir_name in dirs:
            if dir_name == folder_name:
                source_path = os.path.join(root, dir_name)
                relative_path = os.path.relpath(source_path, source_dir)
                destination_path = os.path.join(destination_dir, relative_path)

                print('source_path: ', source_path)
                print('relative_path: ', relative_path)
                print('destination_path: ', destination_path)
                
                # Ensure the destination directory exists
                os.makedirs(destination_path, exist_ok=True)
                
                # Copy the folder (including its contents)
                # shutil.copytree(source_path, destination_path)
                distutils.dir_util.copy_tree(source_path, destination_path)

# Example usage:
source_directory = r'/path/to/source_directory'
destination_directory = r'/path/to/destination_directory'
folder_to_copy = 'folder_name'

copy_folders_by_name(source_directory, destination_directory, folder_to_copy)
