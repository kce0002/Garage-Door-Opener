import RPi.GPIO as GPIO 
import time

# Kyle Ehlers
# 
# garage_door.py
# 
# This program sends a high voltage out of a GPIO pin on a raspberry pi 3 to open a garage door
# from a local website.
#
# Modified: 12/24/17

# Clarify that GPIO pin #s are being used, not board pin #s
GPIO.setmode(GPIO.BCM) 

# Disable warnings
GPIO.setwarnings(False) 

# Setup for GPIO pin 18
GPIO.setup(18, GPIO.OUT) 

# Send high voltage through GPIO pin 18
GPIO.output(18, GPIO.HIGH) 

# Pause for 1 second
time.sleep(1) 

# Send low voltage through GPIO pin 18
GPIO.output(18, GPIO.LOW) 