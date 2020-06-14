import os, time

cam_directory = "./files/"                                 # Directory where the video files are located.
seconds_per_week = 1200                                 # 604800                           
one_week_prior = time.time() - seconds_per_week     
files = os.listdir(cam_directory)


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
    global cam_directory
    global files
    for file in files: 
        mtime = os.path.getmtime(cam_directory + file)              #get mtime (last time the file's contents were changed)
        if mtime <= one_week_prior: 
            os.remove(cam_directory + file)


if __name__ == "__main__":
    newFiles = set(files) - set(getOldDirectoryContents())
    for newFile in newFiles:
        sendEmail(newFile)
    deleteOldFiles()
    saveDirectoryContents()