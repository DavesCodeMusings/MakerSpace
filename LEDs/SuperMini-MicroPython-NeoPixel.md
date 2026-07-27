# WS2812B (NeoPixel) Addressable LED Basics
This guide is a quick introduction to controlling the single built-in NeoPixel on the SuperMini ESP32-S3 board. Other ESP boards with built-in NeoPixels should work as long as you adjust the code for the correct GPIO pin connection.

## Prerequisites
* ESP32-S3 SuperMini with WS2812B (NeoPixel)
* Host computer capable of accessing MicroPython's REPL prompt
* USB-A to USB-C cable for power and communication

## Code
The following code snippets can be typed directly into the MicroPython Read Evaluate Print Loop (REPL) prompt. It's the thing that looks like this: **>>>**

First, we need to import the _machine_ module to be able to control the General Purpose Input/Output (GPIO) line connected to the NeoPixel.

```py
import machine
```

Next, we'll configure the GPIO pin properties. The GPIO number is printed on the SuperMini board next to the small white square that is the NeoPixel. The examples here assume GPIO pin 48. If your NeoPixel has a different label, use that in place of 48 in the code below.

```py
pin = machine.Pin(48, machine.Pin.OUT)
```

Then, we can configure the NeoPixel properties by importing the module and defining a variable to reference the NeoPixel. This tells the program which pin to use and how many NeoPixels are connected.

```py
import neopixel
np = neopixel.NeoPixel(pin, 1)
```

Finally, we can access the _np_ variable to controll the NeoPixel's color and brightness. The example below sets the color to red at one-quarter brightness. 

```py
np[0] = (64, 0, 0)
np.write()
```

## More Colors
Try showing different colors and combinations. The three numbers represent RED, GREEN,  BLUE, in that order. The values control the brightness and can be between 0 and 255. Be sure to use _np.write()_ each time to make the change take effect.

```py
np[0] = (0, 64, 0)
np.write()
```

```py
np[0] = (0, 0, 64)
np.write()
```

```py
np[0] = (64, 64, 0)
np.write()
```

```py
np[0] = (0, 64, 64)
np.write()
```

```py
np[0] = (64, 0, 64)
np.write()
```

After finishing the examples above, take a look at an [html color code chart](https://html-color-codes.com/rgb.php) Experiment with the red, green, and blue values listed there. Note that the results will be close, but not exact. It may help to shine the NeoPixel on a white piece of paper rather than trying to look at it directly.
