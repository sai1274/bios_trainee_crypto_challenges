a= "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d".decode('hex')
for i in range(256):
	z=""
	for j in a:
		z=z+chr(ord(j) ^ord(chr(i)))
	if(z[0]=='c' or z[0]=='C'):
		print(z)	
