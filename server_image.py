import socket
import os
def checkpath(dir):
    newdir = "./"+dir+"/"
    if os.path.isdir(newdir):
        print "the directory file to exists"
        folderName = raw_input("please enter new folder:")
        os.mkdir(str(folderName))
        ispath = str(folderName)
    else:
        print "no this directory",newdir
        os.mkdir(newdir)
        ispath = newdir
    return ispath

address = ("127.0.0.1", 4000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(10)
print "active"
# path = 'c:/store/'
mypath = 'myImage'
mypath = checkpath(mypath)
print(mypath)
# os.chdir(path)
# new = "10"
# os.mkdir(new)
# os.mkdir(mypath)
# thisPath = path+new+"/"
while True:
    data, addr = s.accept()
    print addr
    img = data.recv(1024)
    # f = open(thisPath+"new.png","wb")
    f = open(mypath+"/"+"new.png", "wb")
    # f.write(img)
    while img:
        f.write(img)
        img = data.recv(1024)
        print "Downloading..."
    print "Complete"
    break
data.close()
s.close()
