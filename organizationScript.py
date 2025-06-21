import os, shutil, sys, json

# add main file to organize here
inputDirString = "C:/Users/aleja/Desktop/FileOrganizer"
inputDir = os.path.abspath(inputDirString)

# import values from system arguments if provided
args = sys.argv
if len(args) > 1:
    function = args[1]

OUTPUT_FILE = "personal_output_groups.json"

# default outputGroups which can be modified
# outputGroups = [
#     {
#         "name": "output1",
#         "keywords": ["HW", "TextBook"],
#         "subdirs": {
#             "Math 20E": ["20E"],
#             "Math 103A": ["103A"],
#             "Math 154": ["154"]
#         }
#     },
#     {
#         "name": "output2",
#         "keywords": ["Important", "Alejandro"],
#         "subdirs": {}
#     },
#     {
#         "name": "output3",
#         "keywords": ["Misc", ".pdf", ".docx", ".txt"],
#         "subdirs": {}
#     }
# ]
# Load existing output groups from file if it exists
def load_output_groups():
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r") as file:
            return json.load(file)
    else:
        return []


# save new output group to file
def save_output_groups():
    with open(OUTPUT_FILE, "w") as file:
        json.dump(outputGroups, file, indent=4)


# Creates new outputGroup dictionary (helper function)
def create_output_group(name, keywords, subdirNames = None, subdirValueArrays = None):
    subdir = create_subdir_dict(subdirNames, subdirValueArrays)

    return {
        "name": name,
        "keywords": keywords,
        "subdirs": subdir
    }

# creates subdirectory dictionary (helper function)
def create_subdir_dict(keys = None, valueArrays = None):
    subdir_dict = {}

    if (keys is None) or (valueArrays is None):
        return subdir_dict
    else:
        for key, valueArray in zip(keys, valueArrays):
            subdir_dict[key] = valueArray
        return subdir_dict
    


#add new output group to outputGroups using create_output_group
def add_output_group(name, keywords, subdirNames = None, subdirValueArrays = None):
    new_group = create_output_group(name, keywords, subdirNames, subdirValueArrays)
    outputGroups.append(new_group)
    save_output_groups()
    print(f"Added new output group: {name}")


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

# Function to print current output groups
def print_groups():
    print("Current output groups:")
    for group in outputGroups:
        print(f"Group Name: {group['name']}, Keywords: {group['keywords']}, Subdirs: {group['subdirs']}")

outputGroups = load_output_groups()

# Main loop if no arguments are provided
if(len(args) <= 1):
    moved_files = 0
    for file in os.listdir(inputDir):
        path = os.path.join(inputDir, file)
        if os.path.isfile(path):
            if move_file_to_output(path, file):
                moved_files += 1

    # Print the number of files moved
    print(f"\nTotal files moved: {moved_files}")

elif(function == 'addGroup'):
    # Template:
    # add_output_group(name, keywords, subdirNames = None, subdirValueArrays = None)

    if(len(args) != 2):
        print("Please only provide the function name 'addGroup' to add a new output group.")

    name = input("Please enter the name of the new output group: ")
    keywords = input("Please enter the keywords for the new output group as comma seperated valyes: ").replace(" ", "").split(',')
    has_subdirs = input("Does this output group have subdirectories? (yes/no): ").strip().lower()

    if has_subdirs == 'yes':
        numOfSubdirs = input("How many subdirectories does this output group have? ")

        for i in range(int(numOfSubdirs)):
            subdirName = input(f"Please enter the name of subdirectory {i+1}: ")
            subdirValues = input(f"Please enter the keywords for subdirectory {subdirName} as comma separated values: ").replace(" ", "").split(',')
            
            if i == 0:
                subdirNames = [subdirName]
                subdirValueArrays = [subdirValues]
            else:
                subdirNames.append(subdirName)
                subdirValueArrays.append(subdirValues)
    else:
        subdirNames = None
        subdirValueArrays = None

    # Now with all attained information, we can add the output group
    add_output_group(name, keywords, subdirNames, subdirValueArrays)

    #Let user know that the output group was added
    print(f"Output group '{name}' added with keywords {keywords} and subdirs {subdirNames if subdirNames else 'None'}.")
    print_groups()
            
elif(function == 'printGroups'):
    print_groups()


