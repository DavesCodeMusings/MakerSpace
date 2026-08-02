# Demo program that shows how to read temperature and humidity from
# an SHT30 (or compatible) sensor wired on the Inter-IC (I2C) bus.

from micropython import const
from machine import Pin, SoftI2C
from time import sleep_ms
from sht3x import SHT3x


# Adjust as needed for your boards.
I2C_CLOCK = const(4)
I2C_DATA = const(5)

# This is the default address for SHT30
I2C_ADDR = const(0x44)

i2c = SoftI2C(scl=Pin(I2C_CLOCK), sda=Pin(I2C_DATA))
if I2C_ADDR not in i2c.scan():
    print(f"No device found at {I2C_ADDR}")
sht3x = SHT3x(i2c, addr=I2C_ADDR, debug=True)
sht3x.reset()
sleep_ms(SHT3x.COMMAND_WAIT_TIME_mS)  # Must wait before sending another command.
sht3x.clear_status()
sleep_ms(SHT3x.COMMAND_WAIT_TIME_mS)
sht3x.measure()
sleep_ms(SHT3x.MEASUREMENT_WAIT_TIME_mS)  # Measurement wait time is longer.
try:
    sht3x.read()
except OSError as ex:
    print(f"Data read failed: {ex}")
else:
    print(f"{sht3x.temperature} C")
    print(f"{sht3x.humidity}% RH")
