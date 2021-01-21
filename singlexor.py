f=open("60_strings.txt","r")
for i in f:
	#print(i)
	#a=f.readline()
	#print(a,end="")
	length=len(i)
	a=str(i[:length-1])
	#print(a)
	a=a.decode('hex')
	z=str()
	high_score=int(0)
	org_str=str()
	length=len(a)
	for i in range (97,123):
		score=int(0)
		for k in range(length):
			z = z+ chr(ord(a[k])^ord(chr(i)))
			if( 41 <=ord(a[k])^ord(chr(i)) and 90 >=ord(a[k])^ord(chr(i))):
				score= score +1 
				#print(score,high_score,ord(a[k])^ord(chr(i)))
			if(score>high_score):
				high_score=score
				org_str='' + z	
		#print 'when xored with char : '+chr(i)+' produces the string : '+z
		z=''
	print(org_str)
