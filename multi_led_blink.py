#!/usr/bin/env python

# :) my Led Blink Test 
# LeD Blink Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)
import time
from Netmaxiot import *
# Connect the Netmaxiot LED to digital port D4,D5,D6
led0 = 5
led1 = 6
led2 = 7
pinMode(led0,"OUTPUT")
pinMode(led1,"OUTPUT")
pinMode(led2,"OUTPUT")
while True:
    try:
        #Blink the LED
        digitalWrite(led0,1)		# Send HIGH to switch on LED
        digitalWrite(led1,1)		# Send HIGH to switch on LED
        digitalWrite(led2,1)		# Send HIGH to switch on LED
        print ("LEDs ON!")
        time.sleep(1)

        digitalWrite(led0,0)		# Send LOW to switch off LED
        digitalWrite(led1,0)		# Send LOW to switch off LED
        digitalWrite(led2,0)		# Send LOW to switch off LED
        print ("LEDs OFF!")
        time.sleep(1)

    except IOError:				# Print "Error" if communication error encountered
        print ("Error")
