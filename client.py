import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

BUFFER_SIZE = 1024
num = raw_input("enter your number: ")
MESSAGE = str(num)
# MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
print"send "+MESSAGE
data = s.recv(BUFFER_SIZE)
print "received data:", data

s.close()
