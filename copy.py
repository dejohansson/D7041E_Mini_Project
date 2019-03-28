import shutil
import os

source = "D:\AI\english"
for dir in os.listdir(source):
    #print(os.path.join(dir))
    #os.listdir(os.path.join(source, dir))
    for subDir in os.listdir(os.path.join(source, dir)):
        for f in os.listdir(os.path.join(source, subDir)):
            print(os.path.join(source, f, f))
            shutil.move(os.path.join(source, f, f), "D:/AI/temp/")