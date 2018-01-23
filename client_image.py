import socket
name = "1"
address = ("127.0.0.1", 4000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
# name = (raw_input("enter your filename"))
path  = "02.jpg"
while True:
    # data, addr = s.accept()
    # print addr
    if name == "1":
        print name
        f = open(path,"rb")
        img = f.read(1024)
        # s.send(img)
        while img:
            s.send(img)
            img = f.read(1024) #please send for img outside loop while
            print "sending..."
        print "sent"
        break

s.close()
