from machine import Pin, SPI ,UART
from ucryptolib import aes
import random
import sdcard
import time
import uos
import os

MODE_CBC = 2
BLOCK_SIZE = 16

spi=SPI(0,sck=Pin(18),mosi=Pin(19),miso=Pin(16))
sd=sdcard.SDCard(spi,Pin(17))

key = b'this_is_the_key_123456_asdfgh123'

plaintext = 'SB COMPONENTS'

print('Plain Text:', plaintext)

# Padding plain text with space 
pad = BLOCK_SIZE - len(plaintext) % BLOCK_SIZE
plaintext = plaintext + " "*pad

iv = uos.urandom(BLOCK_SIZE)
cipher = aes(key,MODE_CBC,iv)
 
ct_bytes = iv + cipher.encrypt(plaintext)
print ('AES-CBC encrypted:', ct_bytes)


vfs = os.VfsFat(sd)
os.mount(vfs, "/fc")
print("Filesystem check")
print(os.listdir("/fc"))

fn = "/fc/Encripted.bin" # make encripted file

'''
print()
print("Single block read/write")
with open(fn, "ab") as f:
    n = f.write(ct_bytes)
    print(n, "bytes written") 
'''
with open(fn, "rb") as f:
    result2 = f.read()
    print(result2)
    print(len(result2), "bytes read")

print(result2)
iv = result2[:BLOCK_SIZE]
cipher = aes(key,MODE_CBC,iv)
decrypted = cipher.decrypt(result2)[BLOCK_SIZE:]
print('AES-CBC decrypted:', decrypted)
os.umount("/fc")