import os
import shutil
import yaml

class Sorter:

    @staticmethod
    def load_config():
        with open("config.yaml", "r") as file:
            configs = list(yaml.load_all(file, Loader=yaml.FullLoader))
        return configs

    @staticmethod
    def get_files_type_in_folder(extensions, path_to_folder):
        filenames = os.listdir(path_to_folder)
        files = []
        for filename in filenames:
            file = filename.split(".")
            if file[-1] in extensions:
                files.append(path_to_folder + "/" + filename)
        return files

    @staticmethod
    def move_files_containing_keywords_to_folder(list_of_files, keywords, destination_folder):
        if not os.path.isdir(destination_folder):
            os.mkdir(destination_folder)
        for file in list_of_files:
            if keywords != None:
                for keyword in keywords:
                    if keyword.lower() in file.lower():
                        shutil.move(file, destination_folder)
            else:
                shutil.move(file, destination_folder)
