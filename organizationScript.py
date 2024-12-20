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
            #create path if it does not exists
            if(not os.path.exists(outputDir1)):
                os.mkdir(outputDir1)
            #sort through all possible courses
            if(path.find("20E") != -1):
                course1Dir = outputDir1 + "/Math 20E"
                if(not os.path.exists(course1Dir)):
                    os.mkdir(course1Dir)
                shutil.move(path, course1Dir)
            elif(path.find("103A") != -1):
                course2Dir = outputDir1 + "/Math 103A"
                if(not os.path.exists(course2Dir)):
                    os.mkdir(course2Dir)
                shutil.move(path, course2Dir)
            elif(path.find("154") != -1):
                course3Dir = outputDir1 + "/Math 154"
                if(not os.path.exists(course3Dir)):
                    os.mkdir(course3Dir) #
                shutil.move(path, course3Dir)
                '''  
            Uncomment this block for course4
            elif(path.find("egcourse") != -1):
                course4Dir = outputDir1 + "egcourse"
                if(not os.path.exists(course4Dir)):
                    os.mkdir(course4Dir)
                shutil.move(path, course4Dir)
                   '''
            else:
                shutil.move(path, outputDir1)
                
        #Important documents
        elif(path.find("Important") != -1 or path.find("Alejandro") != -1):
            if(not os.path.exists(outputDir2)):
                os.mkdir(outputDir2)
            shutil.move(path, outputDir2)
        #Other documents
        elif(path.find(".pdf") != -1):
            if(not os.path.exists(outputDir3)):
                os.mkdir(outputDir3)
            shutil.move(path, outputDir3)
        

