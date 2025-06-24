import os, shutil, sys, json
import organizationScriptFunctions as functions
import config



# import values from system arguments if provided
args = sys.argv
if len(args) > 1:
    function = args[1]


    
# Main loop when running script in terminal
if __name__ == "__main__":
    # Run preliminary functions:
    functions.load_data()
    config.inputDirString = config.data.get("inputDirString")
    config.outputGroups = functions.load_output_groups()
    functions.check_input_directory()
    functions.printHelpMenu()

    while True:
        user_input = input("\nEnter a command (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break 

        # Main loop if no arguments are provided
        if(len(user_input) <= 1):
            moved_files = 0
            for file in os.listdir(config.inputDir):
                path = os.path.join(config.inputDir, file)
                if os.path.isfile(path):
                    if functions.move_file_to_output(path, file):
                        moved_files += 1

            # Print the number of files moved
            print(f"\nTotal files moved: {moved_files}")

        elif(user_input == 'addGroup'):
            functions.addGroup()
                    
        elif(user_input == 'printGroups'):
            functions.print_groups()

        elif(user_input == 'changeDirectory'):
            functions.changeDirectory()

        elif(user_input == 'revert'):
            functions.revert_to_default_data()

        elif(user_input == 'clearGroups'):
            functions.clear_groups()

        elif(user_input == 'help'):
            functions.printHelpMenu()



