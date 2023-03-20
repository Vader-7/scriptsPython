import pathlib
import os

print(os.getcwd())


def rename_files():
    folder_path = pathlib.Path('/Users/ty/Downloads/Fotos')
    print(f"Processing files in folder: {folder_path.absolute()}")
    for file_path in folder_path.iterdir():
        if file_path.is_file():
            file_name_parts = file_path.name.split(' ')
            if len(file_name_parts) > 1:
                # Replace the original file name with only the first part before space and default prefix
                new_file_name = f"{file_name_parts[0]}"
                file_path.rename(file_path.with_name(new_file_name))
        else:
            # If it's a directory, call the same function recursively
            rename_files(file_path)
    print('Done')


if __name__ == '__main__':
    rename_files()
