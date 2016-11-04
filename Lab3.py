from pyDes import *
import base64

#Q1

'''
Key      : '12345678'
Plaintext     : AAAABBBBAAAABBBB
Encrypted: '\x19\xffF7\xbb/\xe7|\x19\xffF7\xbb/\xe7|'
Ciphertext     : 19FF4637BB2FE77C19FF4637BB2FE77C
Decrypted     : '9\x07\xa6\xc1\xd7\xac\x13\xda-\xd0\x98\x8aC\x8d'j9\x07\xa6\xc1\xd7\xac\x13\xda-\xd0\x98\x8aC\x8d'j'
'''

#creating a function to handle the diffenernt modes of DES

def DES(msg,mode,e_or_d):
        if mode == 'ECB':
                #msg = msg.encode('utf8')
                #msg=msg.decode('unicode_escape')
                #Setting the DES algorithm
                k = des("12345678", mode)
                #Have to use getKey because the key was converted to binary in the algorithm
                print ("Key      : %s" % k.getKey())
                print ("Message     : %s" % msg)
                #Encrypting the message
                if e_or_d == 'encrypt':
                        e = k.encrypt(msg)
                        #e = e.decode('utf-8')
                        #e=e.decode('unicode_escape')
                        
                        print ("Encrypted: %r" % base64.b16encode(e))
                if e_or_d == 'decrypt':
                        #Decrypting the encrypted ciphertext
                        d = k.decrypt(msg)
                        
                        print ("Encrypted: %r" % base64.b16encode(d))
        if mode == 'CBC':
                k=des("12345678", CBC, "00000000", pad=None, padmode=PAD_PKCS5)
                print ("Key      : %s" % k.getKey())
                print ("Message     : %s" % msg)
                if e_or_d == 'encrypt':
                        e = k.encrypt(msg)
                        #e = e.decode('utf-8')
                        #e=e.decode('unicode_escape')
                        print ("Encrypted: %r" % base64.b16encode(e))
                if e_or_d == 'decrypt':
                        #Decrypting the encrypted ciphertext
                        d = k.decrypt(msg)
                        print ("Decrypted: %r" % base64.b16encode(d))
msg = 'AAAABBBBAAAABBBB'
DES(msg,'ECB','encrypt')
print()
msg = '19FF4637BB2FE77C19FF4637BB2FE77C'
DES(msg,'ECB','decrypt')
print()
msg = b'AAAABBBBAAAABBBB'
DES(msg,'CBC','decrypt')
print()
msg = b'AAC823F6BBE58F9EAF1FE0EB9CA7EB08'
DES(msg,'CBC','encrypt')
