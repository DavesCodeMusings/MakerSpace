# Connect ESP32 to WiFi access point.
# Released to public domain by David Horton. No warranty expressed or implied.
# To use:
# 1. Copy the contents of this file to ESP's boot.py
# 2. Create config.py in the same directory as boot.py
# 3. Define variables for SSID and PASS in config.py

from network import WLAN, STA_IF
from time import ticks_ms
from micropython import const
from config import SSID, PASS

TIMEOUT = const(30)  # seconds

wlan = WLAN(STA_IF)
wlan.active(True)
wlan.connect(SSID, PASS)
start_time = ticks_ms()
while not wlan.isconnected():
    if (ticks_ms() - start_time > TIMEOUT * 1000):
        break
if (wlan.isconnected()):
    print(f"Connected to {SSID} as {wlan.ifconfig()[0]}")
else:
    print(f"Connection to {SSID} timed out.")
