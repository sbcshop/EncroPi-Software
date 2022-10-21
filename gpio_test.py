from machine import Pin
import utime,time

status = machine.Pin(25, machine.Pin.OUT)
gp4 = machine.Pin(4, machine.Pin.OUT)
gp5 = machine.Pin(5, machine.Pin.OUT)
gp14 = machine.Pin(14, machine.Pin.OUT)
gp15 = machine.Pin(15, machine.Pin.OUT)

status.value(1)
gp4.value(1)
gp5.value(1)
gp14.value(1)
gp15.value(1)

