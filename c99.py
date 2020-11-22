import os 
import shutil
#os.system("date")
#os.mkdir("videos")
#os.getcwd()
#print(os.getcwd())
#path = 'C:/Users/User/pythonfiles/c99.py'
#isExist= os.path.exists
#print(isExist)
#root_ext=os.path.splitext(path)
#print(root_ext[0])
#print(root_ext[1])
#path2 = '/Users/User/pythonfiles'
#print("before copying files")
#print(os.listdir(path2))
#source = '/Users/User/pythonfiles/file.txt'
#destination = '/Users/user/pythonfiles/filecopy.txt'
#dest=shutil.copy(source,destination)
#print("after copying files")
#print(os.listdir(path2))
#print("before moving files")
#path3 = '/Users/User/pythonfiles/videos'
#print(os.listdir(path3))
#source1 = '/Users/User/pythonfiles/videos/mp4'
#destination1 = '/Users/user/pythonfiles/videos/png'
#dest1 = shutil.move(source1,destination1)
#print(" after moving files")
#print(os.listdir(path3))
path = input("enter the name of directory to bo sorted")
list_of_files = os.listdir(path)
for file in list_of_files:
    name, ext = os.path.splitext(file)
    ext = ext[1:]

    if ext == '':
        continue

    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file) 
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)