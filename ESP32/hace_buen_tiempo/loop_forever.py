# Demo program showing how to run a program in a continuous loop.

from time import sleep

print("Running... (Use CTRL+C to stop.)")
while True:
    sleep(1)
    print("Still running.")
