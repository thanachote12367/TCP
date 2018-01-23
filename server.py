
import socket
def factorial(n):
    # print(n)
    if int(n) == 0:
        return 1
    else:
        c = int(n) * factorial(int(n)-1)
        # print type(c)
        return c

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

print "active...."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print 'address:{}'.format(addr)

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    c = factorial(data)
    conn.send(str(c))  # echo
    print "sent to "+str(c)

conn.close()