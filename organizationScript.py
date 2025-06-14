import os, shutil

#add main file to organize here
inputDirString = "C:/Users/aleja/Desktop/FileOrganizer"
inputDir = os.path.abspath(inputDirString)

outputGroups = [
    {
        "name": "output1",
        "keywords": ["HW", "TextBook"],
        "subdirs": {
            "Math 20E": ["20E"],
            "Math 103A": ["103A"],
            "Math 154": ["154"]
        }
    },
    {
        "name": "output2",
        "keywords": ["Important", "Alejandro"],
        "subdirs": {}
    },
    {
        "name": "output3",
        "keywords": ["Misc", ".pdf", ".docx", ".txt"],
        "subdirs": {}
    }
]

# All subfunctions that will feed into main loop here:
def checkPathExists(path):
    if not os.path.exists(path):
        os.makedirs(path)

# returns True if filename contains any of the keywords
def matches_any_keyword(filename, keywords):
    name, ext = os.path.splitext(filename)
    #return true if at least one keyword is a match
    for keyword in keywords:
        if (keyword in name) or (keyword == ext):
            return True
    #else:
    return False

# moves file to correct output and returns True if successful
def move_file_to_output(filePath, fileName):
    for current_Output in outputGroups:
        # Check if file matches any of the keywords
        if matches_any_keyword(fileName, current_Output["keywords"]):
            base_output = os.path.join(inputDir, current_Output["name"])
            checkPathExists(base_output)

            # Try to match subdirectory
            for subdir, sub_keywords in current_Output["subdirs"].items():
                if matches_any_keyword(fileName, sub_keywords):
                    full_subdir = os.path.join(base_output, subdir)
                    checkPathExists(full_subdir)
                    shutil.move(filePath, os.path.join(full_subdir, fileName))
                    print(f"Moved {fileName} to {full_subdir}")
                    return True

            # No match found, move into base folder
            shutil.move(filePath, os.path.join(base_output, fileName))
            print(f"Moved {fileName} to {base_output}")
            return True
    return False

# Main loop
moved_files = 0
for file in os.listdir(inputDir):
    path = os.path.join(inputDir, file)
    if os.path.isfile(path):
        if move_file_to_output(path, file):
            moved_files += 1


# Print the number of files moved
print(f"\nTotal files moved: {moved_files}")

            

