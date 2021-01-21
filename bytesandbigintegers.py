#from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes
int_msg= raw_input()
print(long_to_bytes(int_msg))
