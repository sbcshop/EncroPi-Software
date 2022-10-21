# In this example we have two AES Mode ECB,CBC and CTR
import uos
from ucryptolib import aes
 
ECB_MODE = 1
CBC_MODE = 2
CTR_CTR = 6
BLOCK_SIZE = 16
 
# key size must be 16 or 32
# key = uos.urandom(32) # or you can use random key
key = b'this_is_the_key_123456_asdfgh123'

###################################################
#             AES ECB Cryptographic               #
###################################################
cipher = aes(key, ECB_MODE)
 
plaintext = 'SB COMPONENTS'
print('Plain Text:', plaintext)

# Padding plain text with space 
pad = BLOCK_SIZE - len(plaintext) % BLOCK_SIZE
plaintext = plaintext + " "*pad


encrypted = cipher.encrypt(plaintext)
print('AES-ECB encrypted:', encrypted )
 
cipher = aes(key,1) # cipher has to renew for decrypt 
decrypted = cipher.decrypt(encrypted)
print('AES-ECB decrypted:', decrypted)
 

print('\n\r')

###################################################
#             AES CBC Cryptographic               #
###################################################
 
# Generate iv with HW random generator 
iv = uos.urandom(BLOCK_SIZE)
cipher = aes(key,CBC_MODE,iv)
 
ct_bytes = iv + cipher.encrypt(plaintext)
print ('AES-CBC encrypted:', ct_bytes)
 
iv = ct_bytes[:BLOCK_SIZE]
print(iv)
cipher = aes(key,CBC_MODE,iv)
decrypted = cipher.decrypt(ct_bytes)[BLOCK_SIZE:]
print('AES-CBC decrypted:', decrypted)