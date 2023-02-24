import unittest
from ransom import Encryption
import socket
import os
import random
from ransom import Decryption

class TestRansom(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #Test for the IP Address
    def test_ip(self):
        self.ip= '192.168.56.1'
        hostname = os.getenv("COMPUTERNAME")
        self.assertEqual(socket.gethostbyname(hostname), self.ip)

    #Test for the Random Key generated or not.
    def test_randkey(self):
        self.key = '8mZ?VkG2YRgf{yI7|[xjQGv1khNVpu?Oww:{mRyINEyIv9JmWQOHDAHyyK{bF3i5'
        key = ''
        encryption_level = 512 // 8
        char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789<>?,./:;[]}{|'
        char_pool_len = len(char_pool)
        for i in range(encryption_level):
            key += char_pool[random.randint(0, char_pool_len-1)]
        self.assertNotEqual(key, self.key)
  

    #Test for connection to the server
    def test_server(self):
        self.port1 = 5666
        self.ip_address1 = '192.168.56.1'
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip_address1, self.port1))
        except ConnectionRefusedError:
            self.fail("No connection to the server")
        finally:
            s.close()

    # #Test for checking the decryption key stored in database
    def test_decryption(self):
        self.key = '.hAiMEHu{GPqtt?k,.BOItxxFV4<m}qePW<Olzz4IDWq<2Qp<mz}DV?]J:qmlmY>'
        Decryption.database(self)
        result = Decryption.database(self)
        self.assertEqual(result, self.key)
        
if __name__ == '__main__':
    unittest.main()
