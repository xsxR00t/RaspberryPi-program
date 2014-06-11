#! /usr/bin/python
# -*- coding: utf-8 -*-
# @data  : 2014/6/10
# @author: Katsuya Yamaguchi

import pygame
from pygame.locals import *
import time
import RPi.GPIO as GPIO

def gpioInit():
	GPIO.setmode( GPIO.BCM )
	GPIO.setup( 17, GPIO.OUT )

def main():
	joys = pygame.joystick.Joystick(0)
	joys.init()

	pygame.init()
	print "pygame initialized"

	while True:
		# Joystick chataling
		time.sleep( 0.1 )

		for e in pygame.event.get():
			if e.type == pygame.locals.JOYBUTTONDOWN:
				if e.button == 0:
					GPIO.output( 17, True )
				else:
					GPIO.output( 17, False )
				print "Down at %s" % str( e.button )
                        '''
                        elif e.type == pygame.locals.JOYAXISMOTTION:
				( x, y, x1, y1 ) = joys.get_axis(0), joys.get_axis(1), joys.get_axis(2), joys.get_axis(3)
				print "x, y = (%f, %f) (%f, %f)" % (x, y, x1, y1)

			elif e.type == pygame.locals.JOYHATMOTION:
				( x, y ) = joys.get_hat(0)
				print "Hat Motion %d" % ( e.button )
			'''

if __name__ == '__main__':
	gpioInit()
	pygame.joystick.init()
	main()
