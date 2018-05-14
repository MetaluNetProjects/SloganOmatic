#!/bin/python  
# Simple script for shutting down the raspberry Pi at the press of a button.  
# by Inderpreet Singh  
      
import RPi.GPIO as GPIO  
import time  
import os  
     
# Use the Broadcom SOC Pin numbers  
# Setup the Pin with Internal pullups enabled and PIN in reading mode.  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
  
# Our function on what to do when the button is pressed  
def Shutdown(channel):  
    GPIO.remove_event_detect(channel)
    time.sleep(.2)
    if(GPIO.input(channel)):
	    channel = GPIO.wait_for_edge(channel, GPIO.FALLING, timeout = 800)
	    if channel is None:
	        os.system("sudo shutdown -h now")
	    else:
	        print('False shutdown-button-press detection (stage 2)!')
	        GPIO.remove_event_detect(channel)
	        GPIO.add_event_detect(channel, GPIO.RISING, callback = Shutdown, bouncetime = 500)
    else:
        print('False shutdown-button-press detection!')
        GPIO.add_event_detect(channel, GPIO.RISING, callback = Shutdown, bouncetime = 500)      

# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(3, GPIO.RISING, callback = Shutdown, bouncetime = 500)  
     
# Now wait!  
while 1:  
    time.sleep(1)  
