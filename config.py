import os, shutil, sys, json

OUTPUT_FILE = "saved_data.json"
BACKUP_FILE = "default_saved_data.json"

# All necessary variables:
data = {}
inputDirString = OUTPUT_FILE["inputDirString"] if "inputDirString" in OUTPUT_FILE else "C:/Users/user/Desktop/<DirectoryToBeOrganized>"
inputDir = os.path.abspath(inputDirString)
outputGroups = []