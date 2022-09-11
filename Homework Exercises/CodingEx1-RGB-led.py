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
secToStay = 5 # How long each part should stay for (in sec)
startTime = time.monotonic() # get current time

# make function to set controls at the beginning of each part
def setControls(brghtness, timePeriod):
    led.brightness = brghtness # set LED brightness
    global secToStay # changing global variable so that value can be accessed outside function
    secToStay = timePeriod # How long each part should stay for (in sec)
    global startTime # changing global variable so that value can be accessed outside function
    startTime = time.monotonic() # get current time

################################## PART 1 #####################################

# set controls for part 1
setControls(0.5, 6)

# led for part 1 - red ambulance light
while (time.monotonic() - startTime) < secToStay:
    led[0] = (255, 0, 0)
    time.sleep(0.11)
    led[0] = (0, 0, 0)
    time.sleep(0.11)

time.sleep(2.5) # wait time before next section starts


################################## PART 2 #####################################

# set controls for part 2
setControls(1, 6)

# make the white light appear slowly
# -> removed because OT lights come on in a split of a second
# i = 0
# for i in range(100):
#     led.brightness = i/100
#     led[0] = (255, 255, 255)
#     i = i+5
    # time.sleep(0.1)

# led for part 2 - constant OT light
while (time.monotonic() - startTime) < secToStay:
    led[0] = (255, 255, 255)
led[0] = (0, 0, 0)

time.sleep(2.5) # wait time before next section starts


################################## PART 3 #####################################

# set controls for part 3
setControls(0.5, 12)

# led for part 3 - the wait time - yellow blinking light
while (time.monotonic() - startTime) < secToStay:

    # fade in the yellow light
    i = 0
    for i in range(50):
        led.brightness = i/100
        led[0] = (255, 255, 0)
    led[0] = (255, 255, 0)
    time.sleep(0.9)

    # fade out the yellow light
    i = 0
    for i in range(50):
        led.brightness = 0.5-i/100
        led[0] = (255, 255, 0)
    led[0] = (0, 0, 0)
    time.sleep(0.9)

time.sleep(1.5) # wait time before next section starts


################################## PART 4 #####################################

# set controls for part 4
setControls(0.3, 4)

# led for part 3 - green ok light
while (time.monotonic() - startTime) < secToStay:
    led[0] = (0, 255, 0)
led[0] = (0, 0, 0)

