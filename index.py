import os
import shutil
ext = []
def get_path(name):
    # accepts two arguments, parent directory(system defined directories) and child directory(arbitrary name, provided the dir is already created )
    print("")
    print("***************  "+name+" PATH ENTRIES "+"  ***************")
    parent_dir_name = input("enter name of parent directory(Downloads,Desktop,Documents ...): ")
    dir_name = input("Enter directory name: ")
    print(dir_name) 
    if dir_name != None :
        dir = parent_dir_name +"/"+dir_name
        env = os.environ.get("HOME")
        path = os.path.join(env,dir)
        # print("\n*****************************************************************"+"\n")
    else:
        path = os.environ.get("HOME")
        # print("\n*****************************************************************"+"\n")
    return path

src = get_path("SOURCE")


dest = get_path("DESTINATION")


def validate_path():
    # validates the provided path and stores the extensions in ext list
    verify = os.path.exists(src)

    if verify:
        files = os.listdir(src)
        for file in files:
            index = file.find(".")
            ext.append(file[index+1:])

    else:
        return "not a valid path" 


def create_folder():
    validate_path()
    for name in ext:
        os.mkdir(dest+"/"+name)
  

def move_files():
    # creates folders base on the file ext received
    create_folder()
    # reads the content of the source directory
    list = os.listdir(src)
    if list:  
        # loops through the content of list and performs equality check
        for i in range(len(list)) :
            for j in range(len(list)):
                index = list[i].find(".")
                ans =list[i][index+1:]
                if ans == ext[j]:
     # moves all files found in th src to dest to their respective folders
                    shutil.move(src+"/"+list[i],dest+"/"+ext[j]) 
        print("*********************************\n*\tACTION SUCCESSFUL\t*\n*********************************")

    else:
        print("No file found")


move_files()