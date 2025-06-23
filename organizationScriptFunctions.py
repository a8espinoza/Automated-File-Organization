import os, shutil, sys, json
import organizationScript as org_script
import config

# Ensures that the input directory is set correctly
def check_input_directory():
    if config.inputDirString == "C:/Users/user/Desktop/<DirectoryToBeOrganized>":
        config.inputDirString = input("\nPlease enter the path to the directory you want to organize: ")
        config.inputDir = os.path.abspath(config.inputDirString)
        config.data["inputDirString"] = config.inputDirString

        with open(config.OUTPUT_FILE, "w") as file:
            json.dump(config.data, file, indent=4)

        print(f"Input directory set to: {config.inputDir}")
        print("Please rerun the script with desired function or without arguments to organize files.\n")
        #sys.exit(1)
    else:
        config.inputDir = os.path.abspath(config.inputDirString)
        if not os.path.exists(config.inputDir):
            print(f"\nInput directory does not exist: {config.inputDir}")
            config.inputDirString = input("Please enter the path to the directory you want to organize: ")
            config.inputDir = os.path.abspath(config.inputDirString)
            
            print(f"Input directory set to: {config.inputDir}")
            print("Please rerun the script with desired function or without arguments to organize files.\n")
            config.data["inputDirString"] = config.inputDirString

            with open(config.OUTPUT_FILE, "w") as file:
                json.dump(config.data, file, indent=4)
                #sys.exit(1)
        else:
            print(f"\nInput directory currently set to: {config.inputDir}")

        config.data["inputDirString"] = config.inputDirString

        with open(config.OUTPUT_FILE, "w") as file:
            json.dump(config.data, file, indent=4)


# Load existing data from file or create a new one if it doesn't exist
def load_data():
    if os.path.exists(config.OUTPUT_FILE):
        with open(config.OUTPUT_FILE, "r") as file:
            config.data = json.load(file)
    else:
        config.data = {}
        config.data["inputDirString"] = "C:/Users/user/Desktop/<DirectoryToBeOrganized>"
        with open(config.OUTPUT_FILE, "w") as file:
            json.dump(config.data, file, indent=4)

# Load existing output groups from file if it exists
def load_output_groups():
    global data
    if os.path.exists(config.OUTPUT_FILE):
        with open(config.OUTPUT_FILE, "r") as file:
            config.data = json.load(file)
            return config.data.get("outputGroups", [])
    else:
        return []


# save new output group to file
def save_output_groups():
    with open(config.OUTPUT_FILE, "w") as file:
        config.data["outputGroups"] = config.outputGroups
        json.dump(config.data, file, indent=4)


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
    config.outputGroups.append(new_group)
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
    for current_Output in config.outputGroups:
        # Check if file matches any of the keywords
        if matches_any_keyword(fileName, current_Output["keywords"]):
            base_output = os.path.join(config.inputDir, current_Output["name"])
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
    # If no match found, remain in the input directory
    return False


# Function to add a new output group
def addGroup():
    if(len(org_script.args) != 2):
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


# Function to print current output groups
def print_groups():
    print("Current output groups:")
    for group in config.outputGroups:
        print(f"Group Name: {group['name']}, Keywords: {group['keywords']}, Subdirs: {group['subdirs']}")

# Function to change the input directory
def changeDirectory():
    config.inputDirString = input("Please enter the new path to the directory you want to organize: ")
    config.inputDir = os.path.abspath(config.inputDirString)

    if not os.path.exists(config.inputDir):
        print(f"\nInput directory does not exist: {config.inputDir}")
        #sys.exit(1)
    else:
        print(f"\nInput directory set to: {config.inputDir}")

    config.data["inputDirString"] = config.inputDirString

    with open(config.OUTPUT_FILE, "w") as file:
        json.dump(config.data, file, indent=4)


# revert back to default outout groups and input directory:
def revert_to_default_data():
    if os.path.exists(config.BACKUP_FILE):
        with open(config.BACKUP_FILE, "r") as file:
            config.data = json.load(file)
    
    config.inputDirString = config.data["inputDirString"]
    config.outputGroups = config.data["outputGroups"]

    with open(config.OUTPUT_FILE, "w") as file:
        json.dump(config.data, file, indent=4)

    print("Reverted to default settings.")


# Function to print help menu
def printHelpMenu():
    print("\n")
    print("Main Function: ")
    print("-  If no arguments are provided, the script will organize files \n"
        "      in the input directory based on existing output groups.")
    print("-  To run the main function, simply run the script without arguments like so: \n"
        "      python organizationScript.py\n")
    print("Available Secondary functions:")
    print("1. addGroup - Add a new output group")
    print("2. printGroups - Print current output groups")
    print("3. help - Show this help message")
    print("4. changeDirectory - Change the input directory to a new path")
    print("5. revert - Revert to default settings")
    print("\n")
    print("To use a secondary function, run the script with the function name as an argument like so: ")
    print("python organizationScript.py <function_name>\n")
