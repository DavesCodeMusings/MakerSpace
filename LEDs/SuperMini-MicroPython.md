# MicroPython LED Basics
This is a short introduction to controlling LEDs with a microcontroller. In this case, it's an ESP32-S3 SuperMini running MicroPython. If you're using a different board, it shouldn't be hard to change the GPIO pins to suit whatever model you're using.

## Prerequisites
* ESP32-S3 SuperMini flashed with MicroPython
* Host computer capable of accessing MicroPython's REPL prompt
* USB-A to USB-C cable for power and communication

> The microcontoller board design has been cloned and distributed by several manufacturers, but not all have the NeoPixel LED. Be sure to check the product description to get a compatible board.

## Code
The following code snippets can be typed directly into the MicroPython Read Evaluate Print Loop (REPL) prompt. It's the thing that looks like this: **>>>**

First, we need to import the _machine_ module to be able to control the General Purpose Input/Output (GPIO) lines that drive the built-in LEDs.

```py
import machine
```

Next, we'll configure the red LED (to the right of the USB connector.) We'll make it an output using pin 48.

```py
led = machine.Pin(48, machine.Pin.OUT)
```

Now, we can happily turn the LED on using software.

```py
led.value(1)
```

And off.

```py
led.vaule(0)
```

But what about dimming?

For that, we need to set up pulse width modulation (PWM). We'll configure the LED labeled dimmer (to the left of the USB connector.)

```py
dimmer = machine.PWM(led)
```

Pulse width modulation is essentially just turning the LED on and off really, really fast. So fast, you can't see it. With PWM, we can set various levels of brightness using different _duty cycles_. Duty cycle is the ammount of time the LED is on compared to the time it's off. In MicroPython for this particular microcontroller board, the values can be between 0 and 1023.

Try a sampling of different values one at a time and observe the effect on LED brightness.

```py
dimmer.duty(1)
dimmer.duty(10)
dimmer.duty(100)
dimmer.duty(0)
```

Values all the way up to 1023 are acceptable, but the SuperMini shares GPIO 48 with the NeoPixel and some PWM values can accidentally trigger it. If that happens, simply unplug the SuperMini from power and start again.
