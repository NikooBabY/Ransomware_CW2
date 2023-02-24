import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created sucessfully")
port = 5666

s.bind(('', port))
print("Socket binded to %s" %(port))

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    msgfromclient= c.recv(1024)
    print(msgfromclient.decode('utf-8'))










