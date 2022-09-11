#Example of blinking the built-in led
#Desrt Media Art, week 2.2
#Shreya Goel

print('Hello Desert!')
print ('lets blink')

import board
import digitalio #gices us access to the pins
import time

print('the basic led is attached to pin ' + str(board.LED))

#this variable gives us access to the hardware pin
led = digitalio.DigitalInOut(board.LED) #what is this?

#set the led pin as output so that we can turn it on/off
led.direction = digitalio.Direction.OUTPUT #what is this?

# uses code from ada fruit
# https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/creating-and-editing-code
# while True:
#     led.value = True
#     time.sleep(0.5) #sleep is freezing your program i.e. delay in arduino
#     led.value = False
#     time.sleep(0.5)
#     print("time is %.1f" % time.monotonic())

#record the starting time
startTime = time.monotonic()

# How long to blink for (in sec)
secToBlink = 5

while (time.monotonic() - startTime) < secToBlink:
    led.value = True
    time.sleep(0.5) #sleep is freezing your program i.e. delay in arduino
    led.value = False
    time.sleep(0.5)
    print(" time is %.1f" % time.monotonic())

print ("All done")
