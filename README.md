# Program which will pull the sources according to the *.ver file information
Check out sources from CVS according to *.ver file

### Prerequisites 
* Python (>= 3.8)
* Cvs is in Path

### Python Scripts inside
* `printVerFiles.py` - prints the path of the *.ver file and corresponding CVS Tag
* `doCheckOutByVerFiles.py` - does the check out based on the `input.txt`

#### Error Handling
`printVerFiles` prints at the end list of the files which does not have CVS information inside.</br>
`doCheckOutByVerFiles` prints at the end list of errors which occurred when processing `cvs checkout` command. </br>
Usually it is an incorrect tag (`no such tag`)


### How to start?
Launch `start.bat` from the command line with arguments:
1. Destination location, e.g. `"E:\Checkout"`
2. Data location, e.g. `"E:\copyComponents\data"`

### Input
Data folder should have the `input.txt` file which contains the information about CVS tags to check out.<br />
This file is filled manually, It can be done using information from the #1 stage of the script (`printVerFiles.py`) .</br>
##### Input file structure
Component name | CVS component path | CVS tag
------------ | ------------- |-----
-------------|-------------|-------------|
AdminClient |adminclient | RST#adminclient#core#4-4-82

### Result
As a result, the program will pull the sources from the CVS to the `destination location`

