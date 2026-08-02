# Scan for I2C devices and print addresses found. This will help determine
# if I2C devices are wired correctly.

from machine import Pin, SoftI2C

# Adjust pins as needed for your board.
i2c_clock = 4
i2c_data = 5

i2c = SoftI2C(scl=Pin(i2c_clock), sda=Pin(i2c_data))

print('Scanning i2c bus...')
devices = i2c.scan()

if (len(devices) == 0):
    print("No i2c devices.")
else:
    print('Devices found:', len(devices))
    for address in devices:  
        print("Address: ", hex(address))
