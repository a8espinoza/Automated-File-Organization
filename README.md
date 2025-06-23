# Automated-File-Organization

This python project can read through a given directory and organize the files inside
by putting them into folders and subfolders which can be customized by the user
via the in terminal functions 

Instructions for Use:
Main Function:
-  If no arguments are provided, the script will organize files
      in the input directory based on existing output groups.
-  To run the main function, simply press enter and the organizer
      will store all files in path as per the given groups

Available Secondary functions:
1. addGroup - Add a new output group
2. printGroups - Print current output groups
3. help - Show this help message
4. changeDirectory - Change the input directory to a new path
5. revert - Revert to default settings


To use a secondary function, type in the function as a single word like so and press enter:
<function_name>

Alternatively: <br />
-  you may edit the saved_data.JSON file directy to change both the output groups
      and the input directory. To do this, you can reference both default_saved_data
      and personal_saved_data to get an idea of how to fill in saved_data
