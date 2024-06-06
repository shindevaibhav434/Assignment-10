'''
Design automation script wich accept two directory names and one file extension.
Copy all files with the specified extension from first directory into second directory.
Second directory should be created at run time.

Usage  : DirectoryCopyExt.py "Demo" "Temp" ".exe"

'''


import os
import sys 
import shutil

def DirectoryCopy(FirstDir,SecondDir,extension):

    try:
        if not os.path.exists(SecondDir):
            os.mkdir(SecondDir)
            print("Secondary directory created successfully..")
        else:
            print("Secondary directory already exists")
    except Exception as eobj:
        pass

    flag2 = os.path.isabs(SecondDir)
    if( flag2 == False):
        SecondDir = os.path.abspath(SecondDir)
        print("Path converted into the absolute path :",SecondDir)

    flag = os.path.isabs(FirstDir)
    if(flag == False):
        FirstDir = os.path.abspath(FirstDir)
        print("Path Converted into the absolute path :",FirstDir)

    exist = os.path.isdir(FirstDir)
    if(exist == True):
        for foldername , subfoldername , filenames in os.walk(FirstDir):
            for files in filenames:
                if files.lower().endswith(extension):
                    src = os.path.join(foldername,files)
                    dest = os.path.join(SecondDir,files)
                    shutil.copy2(src,dest)
                    print(f"Copied: {src} to {dest}")

    else:
        print("First Directory is not directory")

def main():

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform copy directory ")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script ")
            print("Name_of_file Name_of_First_Directory  Name of Second_Directory")

    if(len(sys.argv) == 4):
        try:
            DirectoryCopy(sys.argv[1],sys.argv[2],sys.argv[3])
        except Exception as eobj:
            print("Unable to completed task due to ",eobj)

    else:
        print("Invalid option ")
        print("Use of --h option to get the help and use --u option to get the useage of application")


if __name__ == "__main__":
    main()