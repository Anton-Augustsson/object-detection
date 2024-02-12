import os
import shutil
import random
from scripts.common.paths import paths, files

def delete_all_files(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)
            print(f"Deleted: {file_path}")

def get_file_pairs(directory):
    file_pairs = []
    for filename in os.listdir(directory):
        name, extension = os.path.splitext(filename)
        if extension.lower() == '.jpg':
            xml_file = os.path.join(directory, name + '.xml')
            if os.path.exists(xml_file):
                file_pairs.append((os.path.join(directory, name)))
    return file_pairs

# TODO: change percentage to ratio
def random_copy(file_pairs, destination_folder_train, destination_folder_test, percentage):
    num_files_to_copy = int(len(file_pairs) * percentage)
    selected_pairs = random.sample(file_pairs, num_files_to_copy)
    not_selected_pairs = [file for file in file_pairs if file not in selected_pairs]

    for file in selected_pairs:
        shutil.copy(file + '.jpg', destination_folder_train)
        shutil.copy(file + '.xml', destination_folder_train)

    for file in not_selected_pairs:
        shutil.copy(file + '.jpg', destination_folder_test)
        shutil.copy(file + '.xml', destination_folder_test)


def get_labels():
    # TODO: get labels from label map
    labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
    return labels

def delete_partition_dataset():
    print('Delete:', paths['TRAIN_PATH'], paths['TEST_PATH'])

    delete_all_files(paths['TRAIN_PATH'])
    delete_all_files(paths['TEST_PATH'])


def partition_dataset(ratio):
    labels = get_labels() 
    file_pairs = []

    for label in labels:
        path = os.path.abspath(os.path.join(paths['COLLECTED_IMAGES_PATH'], label))
        file_pairs = file_pairs + get_file_pairs(path)

    random_copy(file_pairs, paths['TRAIN_PATH'], paths['TEST_PATH'], ratio)