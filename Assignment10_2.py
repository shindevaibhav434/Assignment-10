'''
Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extension.
Usage : DirectoryRename.py "Demo" ".txt" ".doc"
'''

import os
import sys

def renameFile(DirName,extension1,extension2):
    flat = ""
    exist = ""

    flag = os.path.isabs(DirName)

    if(flag == False):
        DirName = os.path.abspath(DirName)
        print("Path Converted into the absolute path :",DirName)

    exist = os.path.isdir(DirName)

    if(exist == True):
        for foldername, subfoldername , filenames in os.walk(DirName):
            for files in filenames:
                print(files)
                if files.lower().endswith(extension1):
                    base = os.path.splitext(files)[0]
                    print(base)
                    old_file = os.path.join(foldername,files)
                    files = os.path.join(foldername, base + extension2)
                    
                    os.rename(old_file,files)
                    print("Renamed file is :",files)
                    #print("Renamed file : ",old_file, "to" , new_file)
                    #base = os.path.splitext(files)[0]
                    #files = os.rename(files,base + extension2)
                    #print("Renamed files are :",files)
                    #old_file = os.path.join(foldername,files)
                    #new_file = os.path.join(files, base + extension2)
                    #os.rename(files,base + extension2)
                    #os.rename(old_file,new_file)
                    #print("Renamed file : ",old_file, "to" , new_file)
    else:
        print("Unable to perform ")

def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform rename file extension")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script ")
            print("Name_of_file Name_of_Directory Name of first_Extension Name of Second_Extension")

    if(len(sys.argv) == 4):
        try:
            renameFile(sys.argv[1],sys.argv[2],sys.argv[3])
        except Exception as eobj:
            print("Unable to completed task due to ",eobj)

    else:
        print("Invalid option ")
        print("Use of --h option to get the help and use --u option to get the useage of application")



if __name__ == "__main__":
    main()