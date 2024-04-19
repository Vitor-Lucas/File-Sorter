import os
import datetime
import shutil


def get_empty_directories(directory):
    empty_dirs = []

    for root, directories, files in os.walk(directory):
        if not directories and not files:
            empty_dirs.append(root)

    print(len(empty_dirs))
    return empty_dirs


def get_all_file_paths(directory, allowed_extensions):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if get_file_extension(filepath) in allowed_extensions:
                file_paths.append(filepath)

    print('All files with the extensions: '.join(file_paths))
    return file_paths


def create_dir(path, dir_name):
    full_path = os.path.join(path, dir_name)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"Directory '{full_path}' created successfully.")
    else:
        print(f"Directory '{full_path}' already exists.")


def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension


def get_creation_date(file_path):
    creation_time = os.path.getctime(file_path)
    creation_date = datetime.datetime.fromtimestamp(creation_time)
    return creation_date.strftime("%d/%m/%Y")


def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' successfully renamed to '{new_name}'.")
    except OSError as e:
        print(f"Error: {e}")


def delete_empty_dirs(directory):
    for dir_path in get_empty_directories(directory):
        delete_folder(dir_path)


def delete_folder(folder_path):
    shutil.rmtree(folder_path)
