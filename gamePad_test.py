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

			elif e.type == pygame.locals.JOYBUTTONUP:
				print "Up at %s" % str( e.button )

			elif e.type == pygame.locals.JOYHATMOTION:
				( x, y ) = joys.get_hat(0)
				print 'hat motion %d %d' % ( x, y )

			'''
			elif e.type == pygame.locals.JOYAXISMOTION:
				( x , y ) = joys.get_axis(0), joys.get_axis(1)
                print 'x and y : ' + str(x) + ' , ' + str(y)
			'''

if __name__ == '__main__':
	gpioInit()
	pygame.joystick.init()
	main()
