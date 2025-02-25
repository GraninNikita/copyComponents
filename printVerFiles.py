# This program prints the CVS tag (if it exists) according to the *.ver files, which are located in the ./data folder
import os.path
import sys

incorrectVerFilesArray = []

print(sys.argv)
dataLocation = sys.argv[2]

for root, dirs, files in os.walk(dataLocation):
    for f in files:
        fullpath = os.path.join(root, f)
        if os.path.splitext(fullpath)[1] == '.ver':
            with open(fullpath) as verFile:
                readData = verFile.read()
                if "RST" in readData:
                    print(fullpath + ": " + readData.rstrip())
                else:
                    incorrectVerFilesArray.append(fullpath)
print("\n")

print("The files which does not contain correct information about CVS:")
for s in incorrectVerFilesArray:
    print(s)
