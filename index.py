import os
import pathlib
import shutil

# fileExtension = input("Input file extension: ").lower()

print("***************" + "HOME PATH ENTRIES "+"  ***************")
parent_dir_name = input("enter name of parent directory(Downloads,Desktop,Documents ...): ")

print("***************" + "SUB PATH ENTRIES "+"  ***************")
dir_name = input("Enter directory name: e.g work/designs ")

dir = str(pathlib.Path.home() / (parent_dir_name + "/" +dir_name)) #Path to my test directory

ext = []


def getActiveExtensions(dir):
  files = os.listdir(dir)
  for items in files:
      index = items.rfind(".")
      if items[index:] not in ext:
        ext.append(items[index:])
      
getActiveExtensions(dir)

def CreateFolder(directory):
  try:
    if not os.path.exists(directory):
      new_path = dir + "/" + directory
      os.mkdir(new_path)
  except FileExistsError:
    pass
#Move all files 
def MoveFiles(filename, destination):
  try:
    desc = dir + "/" + destination
    shutil.move(dir +"/"+ filename, desc)
  except FileNotFoundError:
    pass
  
# CreateFolder("Working")   
for item in os.listdir(dir):
  for end in ext:
    if item.endswith(end):
      fileType = end.title().replace('.', '')
      CreateFolder(fileType + " Files")
      MoveFiles(item, fileType + " Files")
print("*********************************\n*\t Sorting Successful: Check Directory to Confirm *********************************")


