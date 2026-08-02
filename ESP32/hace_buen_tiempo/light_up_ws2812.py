from micropython import const
from machine import Pin
from neopixel import NeoPixel
from time import sleep

GPIO = const(48)  # Change if needed to match microcontroller.

RED = const((63, 0, 0))
GREEN = const((0, 63, 0))
BLUE = const((0, 0, 63))
OFF = const((0, 0, 0))

np_gpio = Pin(GPIO, Pin.OUT)
np = NeoPixel(np_gpio, 1)

np[0] = RED
np.write()
sleep(2)
np[0] = GREEN
np.write()
sleep(2)
np[0] = BLUE
np.write()
sleep(2)
np[0] = OFF
np.write()
