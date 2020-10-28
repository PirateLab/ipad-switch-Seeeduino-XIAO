# Use Seeeduino-XIAO to make a switch for an Ipad

The idea was to use Circuitpython on a Seeeduino-XIAO to make a switch (button) and use an iPad on iOS with `Switch Control`

## Hardware

* Seeeduino-XIAO
* USB C Cable
* Cable to short pins
* Switch/button

NB: I use `D0`as input, but it could be D1, D2, etc ...

## Code

coming...

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
