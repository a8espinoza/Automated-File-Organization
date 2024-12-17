import os, shutil
'''
#I need to figure out git first
downloadsDirectory = "C:/Users/aleja/Downloads"
testDirectory = "C:/Users/aleja/Desktop/FileOrganizer"
destinationDirectory = "C:/Users/aleja/Desktop/FileOrganizer/moveHere"
exFile = "C:/Users/aleja/Desktop/FileOrganizer/HW4.pdf"
list = os.listdir(testDirectory) #list of files & directories in path
print(list) #print list
print(os.path.abspath(testDirectory)) #print given path
print(testDirectory)
boolean = os.path.exists(testDirectory)
print(boolean)
#a path can be a directory or a file
#shutil.move(testDirectory + "/HW4_sol.pdf", destinationDirectory)

Everything above is for reference and testing purposes
'''
#add all directories here (a path can be either a directory or directory)
inputDir = "C:/Users/aleja/Desktop/FileOrganizer"
outputDir1 = "C:/Users/aleja/Desktop/FileOrganizer/output1"
outputDir2 = "C:/Users/aleja/Desktop/FileOrganizer/output2"
outputDir3 = "C:/Users/aleja/Desktop/FileOrganizer/output3"
outputDirectories = [outputDir1, outputDir2, outputDir3]


listOfPathsInInput = os.listdir(inputDir)
listofPaths = []
for path in listOfPathsInInput:
    listofPaths.append(inputDir + "/" + path)

print(listofPaths)


for path in listofPaths:
    if(os.path.isfile(path)):
        shutil.move(path, outputDirectories[0])
        