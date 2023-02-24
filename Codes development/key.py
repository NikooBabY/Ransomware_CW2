import random

key = ''
encryption_level = 512 // 8
char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789<>?,./:;[]}{|'
char_pool_len = len(char_pool)

for i in range(encryption_level):
    key += char_pool[random.randint(0, char_pool_len-1)]

print(key)