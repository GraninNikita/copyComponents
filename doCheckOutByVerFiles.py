import os
from subprocess import PIPE, Popen

description = "This program will pull the sources by the information from the Input file"
print(description)

destination = input("Please input the destination path to save the sources (default: current folder)")
if not destination: destination = "."

f = open('data/input.txt')
for line in f:
    lineArray = line.split(" ")
    componentName = lineArray[0]
    componentPath = lineArray[1]
    cvsTag = lineArray[2].rstrip()
    cvsCommand = 'cvs -Q checkout -P -d %(destination)s/%(componentName)s -r %(cvsTag)s dev/%(componentPath)s' % {'destination': destination, 'componentName': componentName, 'cvsTag': cvsTag,
                                                                                                                  'componentPath': componentPath}
    print('Running : ' + cvsCommand)

    p = Popen(cvsCommand, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    if stderr == b'':
        print(componentPath + " repository was successfully checked out!")
    else:
        print(componentPath + " repository check out contains some errors : ")
        print(stderr)
