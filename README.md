# Automated-File-Organization

This python project can read through a given directory and organize the files inside
by putting them into folders and subfolders which can be customized by the user
via the in terminal functions 

## Instructions to find and set directory (folder) to be organized
To locate and set the correct input directory, please follow these steps:  <br />
1. Open File Exploror and navigate to desired directory (folder) .
2. right click on the address bar and select 'Copy address as text'.
3. When the program prompts you for the input directory, paste the copied address.
4. Read the prompt carefully and press enter
5. If you need to change the directory while running, use the 'changeDirectory' function.
6. If you would like to double check if the current input directory is what you desire, use the printDirectory function.

## Instructions for Use:
Main Function:
-  If no arguments are provided, the script will organize files
      in the input directory based on existing output groups.
-  To run the main function, simply press enter and the organizer
      will store all files in path as per the given groups

Available Secondary functions:
1. addGroup - Add a new output group
2. printGroups - Print current output groups
3. printDirectory - Print current input directory
4. changeDirectory - Change the input directory to a new path
5. revert - Revert to default settings
6. clearGroups - Clear all output groups
7. help - Print this help menu
8. directoryHelp - Print directions to find and set the input directory


To use a secondary function, type in the function as a single word like so and press enter:
<function_name>

Alternatively: <br />
-  you may edit the saved_data.JSON file directy to change both the output groups
      and the input directory. To do this, you can reference both default_saved_data
      and personal_saved_data to get an idea of how to fill in saved_data


## Download instructions:

To use this organization tool, download and extract the zip file onto the desktop or whereever you keep your programs. Then, run the file named organizationScript.exe and follow the instructions above