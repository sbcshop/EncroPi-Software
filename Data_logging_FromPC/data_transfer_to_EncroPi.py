from time import sleep
import threading
import logging
import EncroPi
import ctypes
import serial
import time
import logging
import threading

import os

if os.name == "posix":
    COMPORT_BASE = "/dev/"
else:
    COMPORT_BASE = ""
    
s = EncroPi.USB()
s.connect('COM8',9600)

while True:
    data = input('Enter data to store in sd card = ')
    s.transmit_message(data.encode("utf-8")+b'\n\r')
    time.sleep(0.5)