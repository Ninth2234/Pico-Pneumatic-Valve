from machine import Pin
from time import sleep

pin_in1 = Pin(0,Pin.OUT)
pin_in2 = Pin(1,Pin.OUT)

pin_in2.high()

while True:
    pin_in1.high()
    sleep(1)
    pin_in1.low()
    sleep(1)
