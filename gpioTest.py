#! /usr/bin/python
# coding: utf-8
# @author Katsuya Yamaguchi

import RPi.GPIO as GPIO
import time

# IO settings
print "setting GPIO..."
GPIO.setmode( GPIO.BCM )
GPIO.setup( 17, GPIO.OUT )

print "on port"
while True:
	GPIO.output( 17, True )
	time.sleep( 0.5 )
	GPIO.output( 17, True )
	time.sleep( 0.5 )
