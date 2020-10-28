# Import the libraries
import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid

# define output LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# flash the LED when booting
for x in range(0, 5):

    led.value = False
    time.sleep(0.2)
    led.value = True
    time.sleep(0.2)

# configure device as keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# define buttons
d0 = DigitalInOut(board.D0)
d0.direction = Direction.INPUT
d0.pull = Pull.UP

# loop forever
while True:

    if not d0.value:

        led.value = False  # led on
        kbd.send(Keycode.ENTER)
        time.sleep(0.2)  # debounce delay
        led.value = True  # led off
