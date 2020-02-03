# This program will pull the sources from the CVS according to the Input file
from subprocess import PIPE, Popen
import sys

destination = sys.argv[1] if len(sys.argv) > 1 else "./"

dataLocation = sys.argv[2] if len(sys.argv) > 1 else "./data/"
errorsList = []

f = open(dataLocation + '/input.txt')
for line in f:
    lineArray = line.split(" ")
    componentName = lineArray[0]
    componentPath = lineArray[1]
    cvsTag = lineArray[2].rstrip()
    cvsCommand = 'cvs -Q checkout -P -d %(destination)s/%(componentName)s -r %(cvsTag)s dev/%(componentPath)s' % {'destination': destination, 'componentName': componentName, 'cvsTag': cvsTag,
                                                                                                                  'componentPath': componentPath}
    print('Running : ' + cvsCommand + "\n")
    sys.stdout.flush()

    p = Popen(cvsCommand, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    # if there are no errors
    if stderr == b'':
        print(componentPath + " repository was successfully checked out!\n")
        sys.stdout.flush()
    else:
        print(componentPath + " : repository was checked out with errors!\n")
        errorsList.append(stderr)
        errorsList.append("\n")

print("Errors: \n")
for line in errorsList:
    print(line)
