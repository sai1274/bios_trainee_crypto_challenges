z= 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
ct=str()
key= 'ICE'
j=int(0)
for i in range(len(z)) :
	ct = ct + chr(ord(z[i]) ^ ord(key[i%len(key)]))
print ct.encode('hex')
