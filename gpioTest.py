#! /usr/bin/python
# coding: utf-8
# @author Katsuya Yamaguchi

import RPi.GPIO as GPIO
import time

# IO settings
print "setting GPIO..."
GPIO.setmode( GPIO.BCM )
# Ouutput IO
GPIO.setup( 17, GPIO.OUT )
# Input IO
GPIO.setup( 23, GPIO.IN )

print "on port"

while True:
	GPIO.output( 17, True )
	time.sleep( 0.5 )
	GPIO.output( 17, False )
	time.sleep( 0.5 )

	'''
	if( GPIO.input( 23 ) == False ):
		GPIO.output( 17, True )
	'''
