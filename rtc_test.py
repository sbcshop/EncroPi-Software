# this file show and set time
# and also display temperature
from machine import Pin, UART,SPI
import time,utime
import EncroPi

rtc = EncroPi.RTC()
print(rtc.read_time())
rtc.set_time('12:24:00,Thursday,2022-10-20') # set time, after setting time uncomment this line 
print(rtc.temperature())

