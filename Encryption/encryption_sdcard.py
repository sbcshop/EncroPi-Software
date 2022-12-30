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
import time
import EncroPi
import uos
import os
import st7789
import vga1_bold_16x32 as font

MODE_CBC = 2
BLOCK_SIZE = 16

sd=EncroPi.SDCard()
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,135,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)

def info():
    tft.init()
    time.sleep(0.2)
    tft.text(font,"SB COMPONENTS", 15,20)
    tft.fill_rect(15, 60, 210,10, st7789.RED)
    
    tft.text(font,"EncroPi", 15,80,st7789.YELLOW)
    #tft.text(font,"CHECK", 15,100,st7789.YELLOW)
    tft.fill_rect(15, 140, 210, 10, st7789.BLUE)
    time.sleep(2)
    tft.fill(0) #clear screen
    
info()

key = b'this_is_the_key_123456_asdfgh123'

plaintext = 'SB COMPONENTS'

print('Plain Text:', plaintext)
tft.text(font,"Plain Text:", 15,20,st7789.YELLOW)
tft.text(font,plaintext, 15,80,st7789.YELLOW)
time.sleep(2)
tft.fill(0)
# Padding plain text with space 
pad = BLOCK_SIZE - len(plaintext) % BLOCK_SIZE
plaintext = plaintext + " "*pad

iv = uos.urandom(BLOCK_SIZE)
cipher = aes(key,MODE_CBC,iv)
 
ct_bytes = iv + cipher.encrypt(plaintext)
print ('AES-CBC encrypted:', ct_bytes)
tft.text(font,'Encrypted:', 15,20,st7789.YELLOW)
tft.text(font,ct_bytes, 15,80,st7789.YELLOW)
time.sleep(2)
tft.fill(0)


vfs = os.VfsFat(sd)
os.mount(vfs, "/fc")
print("Filesystem check")
print(os.listdir("/fc"))

fn = "/fc/Encripted.bin" # make encripted file


print()
print("Single block read/write")
with open(fn, "ab") as f:
    n = f.write(ct_bytes)
    print(n, "bytes written") 

with open(fn, "rb") as f:
    result2 = f.read()
    print(result2)
    print(len(result2), "bytes read")

print(result2)
iv = result2[:BLOCK_SIZE]
cipher = aes(key,MODE_CBC,iv)
decrypted = cipher.decrypt(result2)[BLOCK_SIZE:]
print('AES-CBC decrypted:', decrypted)
tft.text(font,'Decrypted', 15,20,st7789.YELLOW)
tft.text(font,decrypted, 15,80,st7789.YELLOW)
time.sleep(2)
#tft.fill(0)
os.umount("/fc")
