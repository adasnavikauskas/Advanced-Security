
import base64 

from Crypto.Cipher import DES

def addPadding(data):
	length = 8 -(len(data) % 8)
	data += "\x00"*(length)
	return data

def chunks(longdata, n):
	for i in range(0, len(longdata),n):
		yield longdata[i:i + n]

iv = "00000000"
plain_text = 'AAAABBBBCCCCD'
plain_text_with_padding = addPadding(plain_text)
datasource = dict(enumerate(list(chunks(plain_text_with_padding,9)),
start=1))

hash = iv
for d in datasource:
	des = DES.new(datasource[d], DESC.MODE_ECB)
	cipher_text = des.encrypt(hash)
	hash = "".join(chr(ord(x) ^ ord(y)) for x,y in zip(hash, cipher_text))

print "plaintext: " + plain_text
print "hash (base 16 encoded): " + str(map(".join,
zip(*[iter(base64.b16encode(hash))]*16)))
