'''
Design autiomation script which accept directory name and file extension from user.
Display all files with the extension.

usage : DirectoryFileSearch.py "Demo" .txt

Demo is name of directory and .txt is the extension that we want to search

'''
import os
import sys

def DisplayExctension(DirName,FileExtension):

    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if(exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                if name.lower().endswith(FileExtension):
                    print(os.path.join(name))
                    print(name)

    else:
        print("There is no such directory")

def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This script is used to perform specific file traversal")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of file script :")
            print("Name_of_file name_of_Directory name_of_extension")
            exit()

    if(len(sys.argv) == 3):
        try:
            DisplayExctension(sys.argv[1] ,sys.argv[2] )
        except Exception as eobj:
            print("Unable to perform the task due to ",eobj)

    else:
        print("Invalid option ")
        print("Use of --h option to get the help and use of --u option to get the usage of application")
        exit()

if __name__ == "__main__":
    main()