import os
import pathlib
import shutil

fileExtension = input("Input file extension: ").lower()

dir = str(pathlib.Path.home() / "Downloads/CapaSorter") #Path to my test directory

def CreateFolder(directory):
  try:
    if not os.path.exists(directory):
      new_path = dir + "/" + directory
      os.mkdir(new_path)
  except FileExistsError:
      pass
def MoveFiles(filename, destination):
  desc = dir + "/" + destination
  shutil.move(dir +"/"+ filename, desc)
  pass
# CreateFolder("Working")   
for item in os.listdir(dir):
  if item.endswith(f".{fileExtension}"):
    fileType = fileExtension.title()
    CreateFolder(fileType + " Files")
    MoveFiles(item, fileType + " Files")


# print(dir)