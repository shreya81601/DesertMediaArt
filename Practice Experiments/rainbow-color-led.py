# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board
from rainbowio import colorwheel

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

    led.brightness = 0.3

# while True:
#     led.brightness = (time.monotonic()%100)/100
#     print(led.brightness)
#     ledColor = (time.monotonic()*10)%256
#     led[0] = (ledColor, 255-ledColor, 0)
#     time.sleep(0.5)
#     led[0] = (0, 255, 0)
#     time.sleep(0.5)
#     led[0] = (0, 0, 255)
#     time.sleep(0.5)

# random.random() -> gives b/e 0 and 1, randit(min,max) int

i = 0
while True:
    i = (i + 1) % 256  # run from 0 to 255
    led.fill(colorwheel(i))
    time.sleep(0.05)