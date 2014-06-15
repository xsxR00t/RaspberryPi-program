#! /usr/bin/python
# coding: utf-8
# @author Katsuya Yamaguchi

import RPi.GPIO as GPIO
import time

# IO settings
print "setting GPIO..."
GPIO.setmode( GPIO.BCM )
# Ouutput IO
GPIO.setup( 23, GPIO.OUT )
# Input IO
GPIO.setup( 17, GPIO.IN )

print "on port"

while True:
	GPIO.output( 23, True )
	time.sleep( 0.5 )
	GPIO.output( 23, False )
	time.sleep( 0.5 )

	'''
	if( GPIO.input( 17 ) == False ):
		GPIO.output( 23, True )
	'''
