import os, time

cam_directory = "./files/"                                 # Directory where the video files are located.
seconds_per_week = 604800                           
one_week_prior = time.time() - seconds_per_week             
files = os.listdir(cam_directory)
files_to_delete = (file for file in files if os.path.getmtime(cam_directory + file) <= one_week_prior)  # create generator to determine which files to delete 


def sendEmail(newFile):
    print("Sending mail for file: " + newFile)


def getOldDirectoryContents():
    try:
        with open("ls.data","r") as directory:
            oldfiles = directory.readlines()
            oldfiles = [i.rstrip() for i in oldfiles]
            return oldfiles
    except IOError:
        saveDirectoryContents() 
        getOldDirectoryContents() 


def saveDirectoryContents():
    global files
    with open("ls.data", "w") as directory:
        for file in files:
            directory.write(file)
            directory.write("\n")


def deleteOldFiles():
    for file in files_to_delete:  
            os.remove(cam_directory + file)


if __name__ == "__main__":
    newFiles = set(files) - set(getOldDirectoryContents())
    for newFile in newFiles:
        sendEmail(newFile)
    deleteOldFiles()
    saveDirectoryContents()