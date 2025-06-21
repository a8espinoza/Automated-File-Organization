# Automated-File-Organization

This python project can read through a given directory and organize the files inside
by putting them into folders and subfolders which can be customized by the user
via the in terminal functions 

Instructions for Use:
Main Function:
-  If no arguments are provided, the script will organize files
      in the input directory based on existing output groups.
-  To run the main function, simply run the script without arguments like so: <br />
      python organizationScript.py

Available Secondary functions:
1. addGroup - Add a new output group
2. printGroups - Print current output groups
3. help - Show this help message
4. changeDirectory - Change the input directory to a new path
5. revert - Revert to default settings

To use a secondary function, run the script with the function name as an argument like so: <br />
python organizationScript.py <function_name>
