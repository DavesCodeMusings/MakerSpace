# MicroPython LED Basics
This is a short introduction to controlling LEDs with a microcontroller. In this case, it's an ESP32C3 microcontroller running MicroPython. Unfortunately, the LUAtos board is no longer sold on Amazon, but it should not be hard to change the GPIO pins to suit whatever you're board using.

## Prerequisites
* LUATOS ESP32C3 flashed with MicroPython
* Host computer capable of accessing MicroPython's REPL prompt

## Code
The following code snippets can be typed directly into the MicroPython Read Evaluate Print Loop (REPL) prompt. It's the thing that looks like this: >>>

First, we need to import the _machine_ module to be able to control the General Purpose Input/Output (GPIO) lines that drive the built-in LEDs.

```py
import machine
```

Next, we'll configure the LED labeled D4 on the board (to the right of the USB connector.) We'll make it an output using pin 12.

```py
D4 = machine.Pin(12, machine.Pin.OUT)
```

Now, we can happily turn the LED on using software.

```py
D4.value(1)
```

And off.

```py
D4.vaule(0)
```

But what about dimming?

For that, we need to set up pulse width modulation (PWM). We'll configure the LED labeled D5 (to the left of the USB connector.)

```py
p13 = machine.Pin(13)
D5 = machine.PWM(p13)
```

Pulse width modulation is essentially just turning the LED on and off really, really fast. So fast, you can't see it. With PWM, we can set various levels of brightness using different _duty cycles_. Duty cycle is the ammount of time the LED is on compared to the time it's off. In MicroPython for this particular microcontroller board, the values can be between 0 and 1023.

Try a sampling of different values one at a time and observe the effect on LED brightness.

```py
D5.duty(1)
D5.duty(10)
D5.duty(100)
D5.duty(1000)
D5.duty(0)
```
