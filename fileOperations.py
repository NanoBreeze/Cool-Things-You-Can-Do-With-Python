
from os import rename #used to rename files
from os import remove #used to delete files
from os import listdir #lists all the files and subdirectories in a directory


def write_file(file_name, text):
    file = open(file_name, 'w') #'w' means we will be writing to the file. open(...) overwrites any existing file with same name
    file.write(text)
    file.close() # allows other programs to modify the file


def append_file(file_name, text):
    file = open(file_name, 'a') #'a' also creates a new file if the specified one doesn't already exist
    file.write(text)
    file.close()


def get_file(file_name):
    file = open(file_name, 'r') #'r' ensures we can only read the file and can't write to it
    return file.readlines()


def rename_file(original_name, new_name):
    rename(original_name, new_name) #will throw an exception if a file with new_name already exists


def delete_file(file_name):
    remove(file_name)


if __name__ == '__main__':
    write_file('fileOperations.txt', 'This line is written from write_file(...).\n')

    append_file('fileOperations.txt', 'This line is written from append_file(...).\n')

    lines = get_file('fileOperations.txt')
    print(lines)

    #rename a file
    new_name = 'renamedFileOperations.txt'
    try:
        rename('fileOperations.txt', new_name)
    except:
        print('The file ' + new_name + ' already exists')

    delete_file(new_name)

    #print all files and subdirectories of current directory
    current_directory = '.'
    dirs = listdir(current_directory)
    print(dirs)