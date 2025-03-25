import os


def gen_files_path(directory, target_dir):
    for dirpath, dirname, filenames in os.walk(directory):
        if target_dir in dirname:
            target_path = os.path.join(dirpath, target_dir)
            for root, _, files in os.walk(target_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    yield file_path



directory = 'C:/'

target_dir = 'Python_Basic'

files_generator = gen_files_path(directory, target_dir)

for file_path in files_generator:
    print(file_path)