import os

path = "C:\\Users\\steli\\Desktop\\test.txt"

if(os.path.exists(path)):
    print("that location exists!")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a directory!")
else:
    print("that location doesn't exist")

#Open file
try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

#create and overwritten
text = "Hello\nthis is some text\nhave a good day\n"
with open('test_write.txt','w') as file:
    file.write(text)

#Append text
text = "New text"
with open('test_write.txt','a') as file:
    file.write(text)
with open('test_write.txt') as file:
    print(file.read())

#To copy file
import shutil
shutil.copyfile('test_write.txt','copy.txt') #Scr,dst
# shutil.copy()
# shutil.copy2('test_write.txt','C:\\Users\\steli\\Desktop\\test.txt')

#Delete file
path = 'test_write.txt'
try:
    os.remove(path) #delete file
    os.rmdir(path)  #delete a file or empty folder
    shutil.rmtree(path) #delete files and or folders
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("that folder contains files")
else:
    print(path+"deletion was successful")