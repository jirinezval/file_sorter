from sorter import *

Sorter = Sorter()
configs = Sorter.load_config()

for config in configs:
    source_directories = config["move_files"]["from"]
    target_directory = config["move_files"]["to"]
    try:
        keywords = config["move_files"]["keywords"]
    except KeyError:
        keywords = None
    extensions = config["move_files"]["extensions"]
    print("Sorting file types: ", extensions)
    print("\tSource directories: ", source_directories)
    print("\tTarget directory: ", target_directory)
    print("\tKeywords: ", keywords)
    for source_directory in source_directories:
        files = Sorter.get_files_type_in_folder(extensions, source_directory)
        Sorter.move_files_containing_keywords_to_folder(files, keywords, target_directory[0])