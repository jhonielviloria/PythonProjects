import os

def renameFiles():
    dir = os.getcwd()
    file_type = ".txt"
    new_filename = "sampal"

    i = 1
    for file in os.listdir(dir):
        fullpath = os.path.join(dir, file)
        if os.path.isfile(file) and os.path.splitext(fullpath)[1] == file_type:
            os.rename(file, new_filename + f'{i}' + file_type)
            i += 1

renameFiles()