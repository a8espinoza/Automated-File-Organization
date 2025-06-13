import os, shutil

#add main file to organize here
inputDirString = "C:/Users/aleja/Desktop/FileOrganizer"
inputDir = os.path.abspath(inputDirString)

#add all names of directories you want to create
outputDirectoryNames = ["output1", "output2", "output3"]
numberOfOutputs = len(outputDirectoryNames)

#create all output directories
outputDirectoryLocations = [
    os.path.join(inputDir, name) for name in outputDirectoryNames
]

#outputDir1 = ["HW", "TextBook"]
#outputDir1Subdir = ["Math 20E", "Math 103A", "Math 154"]
#outputDir2 = ["Important", "Alejandro"]
#outputDir2Subdir = []
#outputDir3 = ["Misc", ".pdf", ".docx", ".txt"]
#outputDir3Subdir = []

#In the same order as outputDirectoryLocations, add the keywords that will be used to categorize the files.
outputDirectyKeyWords = [
    ["HW", "TextBook"],
    ["Important", "Alejandro"],
    ["Misc", ".pdf", ".docx", ".txt"],
]
#outputSubDirectories = [outputDir1Subdir, outputDir2Subdir, outputDir3Subdir]

while True:
    listOfPathsInInput = os.listdir(inputDir)  # Get the latest list of files
    moved_files = 0  # Track if we moved anything

    for file in listOfPathsInInput:
        path = os.path.join(inputDir, file)  # Get the full path of the file
        print(path)
        #Move file to given Category Directory
        if(os.path.isfile(path)):
            #loop through all directories
            for i in range(len(outputDirectories)):
                #check if directory exists
                if(not os.path.exists(outputDirectoryLocations[i])):
                    os.mkdir(outputDirectoryLocations[i])
                
                for j in outputDirectories[i]:
                    #check if given path contains given directory name
                    if j in file:  # Check if filename contains a keyword
                        dest_path = os.path.join(outputDirectoryLocations[i], file)
                        #create path if it does not exists
                        shutil.move(path, dest_path)
                        moved_files += 1
                        break


    if moved_files == 0:
        break  # Exit loop if no files were moved

                                

            

