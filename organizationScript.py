import os, shutil
'''
#I need to figure out git first
downloadsDirectory = "C:/Users/aleja/Downloads"
testDirectory = "C:/Users/aleja/Desktop/FileOrganizer"
destinationDirectory = "C:/Users/aleja/Desktop/FileOrganizer/moveHere"
exFile = "C:/Users/aleja/Desktop/FileOrganizer/HW4.pdf"
list = os.listdir(testDirectory) #list of files & directories in path
print(list) #print list
print(os.path.abspath(testDirectory)) #print given path
print(testDirectory)
boolean = os.path.exists(testDirectory)
print(boolean)
#a path can be a directory or a file
#shutil.move(testDirectory + "/HW4_sol.pdf", destinationDirectory)

Everything above is for reference and testing purposes
'''
#add all directories here (a path can be either a directory or directory)
inputDir = "C:/Users/aleja/Desktop/FileOrganizer"
outputDir1 = "C:/Users/aleja/Desktop/FileOrganizer/output1"
outputDir2 = "C:/Users/aleja/Desktop/FileOrganizer/output2"
outputDir3 = "C:/Users/aleja/Desktop/FileOrganizer/output3"
outputDirectories = [outputDir1, outputDir2, outputDir3]


listOfPathsInInput = os.listdir(inputDir)
listofPaths = []
for path in listOfPathsInInput:
    listofPaths.append(inputDir + "/" + path)

print(listOfPathsInInput)
print(listofPaths)


for path in listofPaths:
    #Move file to given Category Directory
    if(os.path.isfile(path)):
        #All Homework
        if(path.find("HW") != -1 or path.find("TextBook") != -1):
            if(path.find("20E") != -1):
                class1Dir = outputDir1 + "/Math 20E"
                print(class1Dir)
                if(not os.path.exists(class1Dir)):
                    os.mkdir(class1Dir)
                shutil.move(path, class1Dir)
            elif(path.find("103A") != -1):
                class2Dir = outputDir1 + "/Math 103A"
                print(class2Dir)
                if(not os.path.exists(class2Dir)):
                    os.mkdir(class2Dir)
                shutil.move(path, class2Dir)
            elif(path.find("154") != -1):
                class3Dir = outputDir1 + "/Math 154"
                print(class3Dir)
                if(not os.path.exists(class3Dir)):
                    os.mkdir(class3Dir) #
                shutil.move(path, class3Dir)
                '''  
            Uncomment this block for class4
            elif(path.find("egclass") != -1):
                class4Dir = outputDir1 + "egclass"
                if(not os.path.exists(class4Dir)):
                    os.mkdir(class4Dir)
                shutil.move(path, class4Dir)
                   '''
            else:
                shutil.move(path, outputDir1)
                
        #Important documents
        elif(path.find("Important") != -1 or path.find("Alejandro") != -1):
            shutil.move(path, outputDir2)
        #Other documents
        elif(path.find(".pdf") != -1):
            shutil.move(path, outputDir3)
        

