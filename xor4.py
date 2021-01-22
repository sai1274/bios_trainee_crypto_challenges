a= "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104".decode('hex')
key='myXORkey'
print(len(a))
for i in range(256):
	if (  chr(ord(a[0]) ^  ord(chr(i))) =='c' ):
		print('c',chr(i))			
	if ( chr(ord(a[1]) ^  ord(chr(i)))=='r' ):
		print('r',chr(i))
	if(   chr(ord(a[2]) ^  ord(chr(i))) =='y' ):
		print('y',chr(i))
	if(   chr(ord(a[3]) ^  ord(chr(i))) =='p' ):
		print('p',chr(i))
	if(   chr(ord(a[4]) ^  ord(chr(i))) =='t' ):
		print('t',chr(i))
	if(   chr(ord(a[5]) ^  ord(chr(i))) =='o' ):
		print('o',chr(i)) 
	if(   chr(ord(a[6]) ^  ord(chr(i))) =='{' ):
		print('{',chr(i))
	if(   chr(ord(a[len(a)-1]) ^  ord(chr(i))) =='}' ):
		print('}',chr(i))
flag=''
for i in range(len(a)):
	flag=flag + chr(ord(a[i]) ^ ord(key[i%len(key)]))
print(flag)
