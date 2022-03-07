from collections import deque
import os
from collections import deque

filesToProcess = deque()

folderName = "Insert Folder Name"

#If script is located at /Desktop and folder is in /Desktop/RootFolder/FolderToProcess, folderName = "RootFolder/FolderToProcess"


#Loops through files in folder and adds them to queue for processing
for root, dirs, files in os.walk("./{}".format(folderName), topdown=False):
    for file in files:
        filesToProcess.append(file)


#Pops each file from queue for processing, hence no repetition
while filesToProcess:
    currFile = filesToProcess.popleft()
    # Do any processing



