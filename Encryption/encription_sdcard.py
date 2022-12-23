'''
#------------------------------------------------------------------------
#
# This is a python Example code for EncroPi Board
# Written by SB Components Ltd 
#
#==================================================================================
# Copyright (c) SB Components Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
'''

from machine import Pin, SPI ,UART
from ucryptolib import aes
import random
import sdcard
import time
import EncroPi
import uos
import os

MODE_CBC = 2
BLOCK_SIZE = 16

sd=EncroPi.SDCard()

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
