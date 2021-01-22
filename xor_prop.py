#from pwm import xor
#print(xor(1,1))
key1='a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313' 
r2='37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
r3='c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
xored='04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
flag=''
key2 = ''
key3 = ''
key1=key1.decode('hex')
r2=r2.decode('hex')
xored=xored.decode('hex')
r3=r3.decode('hex')
for i in range(len(key1)):
	key2=key2 + chr(ord(key1[i]) ^ ord(r2[i]))
print(key2)
for i in range(len(key1)):
	key3=key3 + chr(ord(key2[i]) ^ ord(r3[i]))
print(key3)
for i in range(len(key1)):
	flag=flag + chr((ord(xored[i]) ^ ord(r3[i]))^ord(key1[i]))
print(flag)
