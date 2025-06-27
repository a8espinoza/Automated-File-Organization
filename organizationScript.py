import os, shutil, sys, json
import organizationScriptFunctions as functions
import config


    
# Main loop when running script in terminal
if __name__ == "__main__":
    # Run preliminary functions that only need to be run once:
    functions.load_data()
    config.inputDirString = config.data.get("inputDirString")
    config.inputDir = os.path.abspath(config.inputDirString)
    config.outputGroups = functions.load_output_groups()
    functions.printHelpMenu()

    # ask the user for input until they exit
    while True:
        # preliminary checks that must run every time:
        functions.check_input_directory()


        # Get user input and process it
        user_input = input("\nEnter a command (or 'exit' to quit): ")
        original_input = user_input 
        user_input = user_input.lower().strip().replace(" ", "")

        # Check for exit commands and break
        exitCommands = ['exit', 'quit', '0', 'e', 'q', 'x']
        if (user_input in exitCommands):
            break 

        # Main loop if no arguments are provided (organize all files in the input directory):
        if(len(user_input) < 1):
            moved_files = 0
            for file in os.listdir(config.inputDir):
                path = os.path.join(config.inputDir, file)
                if os.path.isfile(path):
                    if functions.move_file_to_output(path, file):
                        moved_files += 1

            # Print the number of files moved
            print(f"\nTotal files moved: {moved_files}")

        # all other commands:
        elif(user_input == 'addgroup' or user_input == '1'):
            functions.addGroup()
                    
        elif(user_input == 'printgroups' or user_input == '2'):
            functions.print_groups()

        elif(user_input == 'printdirectory' or user_input == '3'):
            functions.print_input_directory()

        elif(user_input == 'changedirectory'  or user_input == '4'):
            functions.changeDirectory()

        elif(user_input == 'revert' or user_input == '5'):
            functions.revert_to_default_data()

        elif(user_input == 'cleargroups' or user_input == '6'):
            functions.clear_groups()

        elif(user_input == 'help' or user_input == '7'):
            functions.printHelpMenu()

        elif(user_input == 'directoryhelp' or user_input == '8'):
            functions.print_input_directory_directions()

        elif(user_input == 'checkdirectory'):
            functions.check_input_directory_validity()
        
        else:
            print(f"\nUnknown command: {original_input}\nPlease try again or type 'help' for a list of commands.")



