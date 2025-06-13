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

#In the same order as outputDirectoryLocations, add the keywords that will be used to categorize the files.
outputDirectyKeyWords = [
    ["HW", "TextBook"],
    ["Important", "Alejandro"],
    ["Misc", ".pdf", ".docx", ".txt"],
]
#outputSubDirectories = [outputDir1Subdir, outputDir2Subdir, outputDir3Subdir]

# Create output directories if they don't exist
for directory in outputDirectoryLocations:
    if not os.path.exists(directory):
        os.mkdir(directory)



listOfPathsInInput = os.listdir(inputDir)  # Get the latest list of files
moved_files = 0  # Track if we moved anything

for file in listOfPathsInInput:
    path = os.path.join(inputDir, file)  # Get the full path of the file
    print(path) # Debugging line to see the file paths

    #Move file to given Category Directory
    if(os.path.isfile(path)):
        moved = False
        #loop through all directories
        for i in range(len(outputDirectoryLocations)):
            #loop through all keywords for given directory
            for keyword in outputDirectyKeyWords[i]:
                #check if given path contains given directory name
                if keyword in file:  # Check if filename contains a keyword
                    dest_path = os.path.join(outputDirectoryLocations[i], file)
                    shutil.move(path, dest_path)
                    moved_files += 1
                    print(f"Moved {file} to {outputDirectoryLocations[i]}")
                    moved = True
                    break #stop after first match
                else:
                    continue
            if moved:
                break                                

            

