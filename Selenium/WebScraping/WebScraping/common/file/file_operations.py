#Import Operating system library
import os
from os import listdir
from os.path import isfile, join

cwd = os.getcwd()

class fileOperations():
    #STatic mathods of files and directories
    @staticmethod
    def ListOfFileAndDirectoriesSpecificPath(path):
        files_directories = os.listdir(path)
        return files_directories

    def ListOfFileAndDirectoriesCurrentDirectory():
        files_directories = os.listdir(os.getcwd())
        return files_directories

    def ListFileCurrentDirectory(fileextension):
        files_directories = os.listdir(os.getcwd())
        list_files = []
        for filename in files_directories:
            if filename.endswith('.'+fileextension):
                list_files.append(filename)            
        return list_files

    def List_of_all_files(path):
        all_files = os.listdir()
        return all_files
