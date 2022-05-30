from lib.Pico_ed import *     #import file
from machine import Pin

leds = Matrix()


while True:
    leds.pixel(0, 0)
    leds.fill(255, )
