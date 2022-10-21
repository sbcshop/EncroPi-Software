# this file read and write data from sd card
from machine import Pin, UART,SPI
import time,utime
import EncroPi
import os

sd=EncroPi.SDCard()
vfs = os.VfsFat(sd)
os.mount(vfs, "/fc")
print("Filesystem check")
print(os.listdir("/fc")) # check the files in sd card

print("Single block read/write")

data = "SB COMPONENTS"
#################################################

with open(fn, "a") as f:  # append data to file
    n = f.write(data)
    print(n, "bytes written")
#################################################

#################################################
with open(fn, "r") as f:  # read data from file
    result = f.read()
    print(result)
    print(len(result), "bytes read")
os.umount("/fc")
#################################################    
