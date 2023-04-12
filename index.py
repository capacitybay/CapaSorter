import os
import pathlib
import shutil

# fileExtension = input("Input file extension: ").lower()
ext = []
# get directory path from the user
def getPath():
    print("\n***************" + "HOME PATH ENTRY "+"  ***************")
    parent_dir_name = input("enter name of parent directory(Downloads,Desktop,Documents ...): ")

    print("\n***************" + "SUB PATH ENTRY "+"  ***************")
    dir_name = input("Enter directory name: e.g work/designs: ")
    
    return str(pathlib.Path.home() / (parent_dir_name.title() + "/" +dir_name)) #Path to my test directory

dir = getPath()

def getActiveExtensions(dir):
      try:
          files = os.listdir(dir)
          for items in files:
              index = items.rfind(".")
              if items[index:] not in ext:
                ext.append(items[index:])
      except FileNotFoundError:
         print('The provided path "'+dir+'" Does not exist')
      
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
def CapaSorter():
  try:
    for item in os.listdir(dir):
      for end in ext:
        if item.endswith(end):
          fileType = end.title().replace('.', '')
          CreateFolder(fileType + " Files")
          MoveFiles(item, fileType + " Files")
    print("**************************************************\n* Sorting Successful: Check Directory to Confirm *\n**************************************************")
  except FileNotFoundError:
    pass


CapaSorter()
