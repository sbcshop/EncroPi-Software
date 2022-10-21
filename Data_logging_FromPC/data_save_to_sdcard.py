#data store to sdcard from pc
from machine import UART,SPI
from machine import Pin
import EncroPi
import st7789
import time,utime
import os

import vga1_8x16 as font1
import vga2_8x8 as font
import vga1_16x32 as font
import vga1_16x16 as font2

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,135,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)


uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

def info():
    tft.init()
    utime.sleep(0.2)
    tft.text(font,"SB-COMPONENTS", 0,0)
    tft.fill_rect(0, 40, 210,10, st7789.RED)
    
    tft.text(font,"EncroPi", 0,55,st7789.YELLOW)
    tft.text(font,"Data Logger", 0,100,st7789.YELLOW)
    tft.fill_rect(0, 90, 210, 10, st7789.BLUE)
    time.sleep(1)
    tft.fill(0) #clear screen
    tft.text(font,"SEND MESSAGE", 5,10,st7789.WHITE)
        
info()

while True:
    data = input()
    uart.write(data)#send data
    tft.text(font,data, 10,60,st7789.YELLOW)
    utime.sleep(0.2)#wait 200ms
    tft.text(font,data, 10,60,st7789.BLACK)
    
    sd=EncroPi.SDCard()
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/fc")
    #print("Filesystem check")
    #print(os.listdir("/fc")) # check the files in sd card
    
    fn = "/fc/File.txt"
    #print("Single block read/write")

    #data = "SB COMPONENTS"
    #################################################

    with open(fn, "a") as f:  # append data to file
        n = f.write(data+'\n')
        #print(n, "bytes written")
    os.umount("/fc")
    #################################################
    '''
    #################################################
    with open(fn, "r") as f:  # read data from file
        result = f.read()
        print(result)
        print(len(result), "bytes read")
    os.umount("/fc")
    #################################################    
    '''