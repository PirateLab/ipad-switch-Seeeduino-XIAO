# Use Seeeduino-XIAO to make a switch for an Ipad

The idea was to use Circuitpython on a Seeeduino-XIAO to make a switch (button) and use an iPad on iOS with `Switch Control`

## Hardware

* Seeeduino-XIAO
* USB C Cable
* Cable to short pins
* Switch/button

### Connection with the switch

![Image of the Seeduinoa-XIAO connection with the switch]()

NB: I use `D0`as input, but it could be D1, D2, etc ...

## Code

### firmware.uf2
This firmware has been modified to work with iOS so you need this one to flash your board and use circuitpython.

### main.py
It's your python code, where the logic is.

### adafruit_hid
You’ll need to add some CircuitPython library into the `lib` folder on your CIRCUITPY drive. You can directly copy the directory `adafruit_hid`or get the following files `__init__.mpy`, `keyboard_layout_us.mpy`, `keyboard.mpy` and `keycode.mpy` (directory `adafruit_hid`) from the [CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20201028/adafruit-circuitpython-bundle-5.x-mpy-20201028.zip "CircuitPython library bundle")

## iOS configuration

Follow Apple guide -> [Switch control](https://support.apple.com/en-us/HT201370 "Switch control")

## Troubleshooting

### How to install Circuitpython on my Seeeduino-XIAO ?
You only need to connect your Seeduino-XIAO to your computer and short two pins.
For more details you can refer to these two links :
* [Wiki Seeedstudio](https://wiki.seeedstudio.com/Seeeduino-XIAO-CircuitPython/ "Wiki Seeedstudio")
* [installing-circuitpython-on-seeeduino-xiao](https://makeandymake.github.io/2020/05/02/installing-circuitpython-on-seeeduino-xiao.html "installing circuitpython on seeeduino-xiao")

### Could I use the standard firmeware form Adafruit for my Seeeduino-XIAO ?
Yes but it will only work on MacOS, Windows (never tried Android and Linux), but *not on iOS*.
To work on iOS, you need to use a modified firmeware -> [Adafruit forum](https://forums.adafruit.com/viewtopic.php?f=60&t=168740 "Adafruit forum")

### I would like to add more button/action ?
Look at Andy's work for exemple -> [seeeduino xiao circuitpython usb hid macro keypad](https://makeandymake.github.io/2020/05/02/seeeduino-xiao-circuitpython-usb-hid-macro-keypad.html "seeeduino xiao circuitpython usb hid macro keypad")

## Ressources

* https://wiki.seeedstudio.com/Seeeduino-XIAO-CircuitPython/
* https://makeandymake.github.io/2020/05/02/installing-circuitpython-on-seeeduino-xiao.html
* https://makeandymake.github.io/2020/05/02/seeeduino-xiao-circuitpython-usb-hid-macro-keypad.html
* https://forums.adafruit.com/viewtopic.php?f=60&t=168740
* https://support.apple.com/en-us/HT201370
