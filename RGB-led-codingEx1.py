# Desert Media Art - Coding Exercise 1 - RGB LED Story
# By Shreya Goel - Mon, 12 September 2022

# this LED show has 4 parts -
# 1. the red fast flickering ambulance light for 5 seconds
# 2. the white bright Operation Theatre (OT) light
# 3. the yellow blinking light for the wait period after operation
# 4. green constant light to indicate succesful operation


# import libraries
import time
import board
import neopixel
from rainbowio import colorwheel

led = neopixel.NeoPixel(board.NEOPIXEL, 1) # assign LED


################################## PART 1 #####################################

# set controls for part 1
led.brightness = 0.5 # set LED brightness
startTime = time.monotonic() # get current time
secToBlink = 6 # How long to blink for (in sec)

# led for part 1 - red ambulance light
while (time.monotonic() - startTime) < secToBlink:
    led[0] = (255, 0, 0)
    time.sleep(0.11)
    led[0] = (0, 0, 0)
    time.sleep(0.11)

time.sleep(3) # wait time before next section starts


################################## PART 2 #####################################

# set controls for part 2
led.brightness = 1 # set LED brightness
startTime = time.monotonic() # get current time
secToStay = 4 # How long the white light should stay for (in sec)

# make the white light appear slowly
# i = 0
# for i in range(100):
#     led.brightness = i/100
#     led[0] = (255, 255, 255)
#     i = i+5
    # time.sleep(0.1)

# led for part 2 - constant OT light
while (time.monotonic() - startTime) < secToBlink:
    led[0] = (255, 255, 255)
led[0] = (0, 0, 0)

time.sleep(2.5) # wait time before next section starts


################################## PART 3 #####################################

# set controls for part 3
led.brightness = 0.3 # set LED brightness
startTime = time.monotonic() # get current time
secToBlink = 12 # How long to blink for (in sec)

# led for part 3 - the wait time - yellow blinking light
while (time.monotonic() - startTime) < secToBlink:

    # fade in the yellow light
    i = 0
    for i in range(100):
        led.brightness = i/100
        led[0] = (255, 255, 0)
    led[0] = (255, 255, 0)
    time.sleep(0.9)

    # fade out the yellow light
    i = 0
    for i in range(100):
        led.brightness = 1-i/100
        led[0] = (255, 255, 0)
    led[0] = (0, 0, 0)
    time.sleep(0.9)

time.sleep(1.5) # wait time before next section starts


################################## PART 4 #####################################

# set controls for part 4
led.brightness = 0.5 # set LED brightness
startTime = time.monotonic() # get current time
secToStay = 3 # How long the white light should stay for (in sec)

# make the green light appear slowly
# i = 0
# for i in range(100):
#     led.brightness = i/100
#     led[0] = (255, 255, 255)
#     i = i+5
    # time.sleep(0.1)

# led for part 3 - green ok light
while (time.monotonic() - startTime) < secToBlink:
    led[0] = (0, 255, 0)
led[0] = (0, 0, 0)


################################## PART 5 #####################################

# rainbow color light for recovery state --> deleted
# i = 0
# while True:
#     i = (i + 1) % 256  # run from 0 to 255
#     led.fill(colorwheel(i))
#     time.sleep(0.025)


