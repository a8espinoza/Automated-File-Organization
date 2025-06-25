import os, shutil, sys, json
import organizationScriptFunctions as functions
import config


    
# Main loop when running script in terminal
if __name__ == "__main__":
    # Run preliminary functions:
    functions.load_data()
    config.inputDirString = config.data.get("inputDirString")
    config.outputGroups = functions.load_output_groups()
    functions.check_input_directory()
    functions.printHelpMenu()

    # ask the user for input until they exit
    while True:
        user_input = input("\nEnter a command (or 'exit' to quit): ")
        original_input = user_input 
        user_input = user_input.lower().strip().replace(" ", "")
        if (user_input == "exit" or user_input == "quit"):
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
        elif(user_input == 'addgroup'):
            functions.addGroup()
                    
        elif(user_input == 'printgroups'):
            functions.print_groups()

        elif(user_input == 'changedirectory'):
            functions.changeDirectory()

        elif(user_input == 'revert'):
            functions.revert_to_default_data()

        elif(user_input == 'cleargroups'):
            functions.clear_groups()

        elif(user_input == 'help'):
            functions.printHelpMenu()
        
        else:
            print(f"\nUnknown command: {original_input}\nPlease try again or type 'help' for a list of commands.")



