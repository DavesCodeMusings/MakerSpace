# Cycle through the primary and secondary RGB colors on ESP32-S3 SuperMini.
# Released to public domain by David Horton. No warranty expressed or implied.

from micropython import const
from machine import Pin
from neopixel import NeoPixel
from time import sleep

GPIO = const(48)  # Change if needed to match microcontroller.

np_gpio = Pin(GPIO, Pin.OUT)
np = NeoPixel(np_gpio, 1)
colors = [
    (127,0,0),
    (63, 63, 0),
    (0,127,0),
    (0, 63, 63),
    (0, 0, 127),
    (63, 0, 63)
]

index = 0
while True:
    np[0] = colors[index]
    np.write()
    sleep(1)
    index += 1
    if index == len(colors):
        index = 0
