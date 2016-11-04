from Crypto.Util import number

p = number.getPrime(16)
q = number.getPrime(16)
m = p * q
t = (p-1)*(q-1)
e = 65537
d = (e^(-1)) % t

print "p = " + str(p)
print "q = " + str(q)
print "m = " + str(m)
print "t = " + str(t)
print "e = " + str(e)
print "d = " + str(d)
print "Public key {m,e}: {" + str(m) + " , " + str(e) + " } "
print "Private key {m,d}: {" + str(m) + " , " + str(d) + " } "

p = 'A'
p_lst = [str(ord(x)).zfill(3) for x in p]
p_lst = int(" ".join(p_lst))

######encryptttttioiiooonn##
c = (p_lst ^ e) % m
recovered = (c ^ d) % m

print "Plaintext: " + str(p_lst)
print "Ciphertext " + str(c)
print "Plaintext: " + str(recovered)

