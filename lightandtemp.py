#!/usr/bin/env python
import Netmaxiot
from time import sleep
#Sensor connected to A0,A1,A2 Port 
x = 0		 
y = 1		 
while 1:
    try:
        read1 = Netmaxiot.analogRead(x)
        read2 = Netmaxiot.analogRead(y)
        sleep (3.0)
        print (" ")
        print ("Reading channel 1=%d"%(read1))
        print ("Reading channel 2=%d"%(read2))
        print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        vol=read1*4.89
        print ("our voltage=%f mv "%(vol))
        print "--------------------------------------"
        temp=vol/10
        light=read2*100/1023
        print "######################################"
        print ("Light intensity=%d Percent "%(light))
        print ("temp=%0.2f *C "%(temp))
        print "_________________________________"
        print " "
    except IOError:
        print ("Error please check you Netmax IOT Shiled and Sensors ")
