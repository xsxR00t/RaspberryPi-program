#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

import pygame
from pygame.locals import *
import time
import RPi.GPIO as GPIO

def initIO() :
	GPIO.setmode(GPIO.BCM)

def main() :
	initIO()
	pygame.init()
	print "Initialized"

	while True :
		time.sleep( 0.1 )
		while True :
			time.sleep( 0.1 )
			# if True :
			# 	pressed_keys = pygame.key.get_pressed()
			# 	val = raw_input("Enter:")
			pressed_keys = pygame.key.get_pressed()
			val = raw_input("Enter:")
			try :
				if val == 'a':
					print "pushed %s" % val
				elif val == 's':
					print "motor1 stop"

				if val == 'b':
					print "pushed %s" % val
				elif val == 'v':
					print "pushed %s" % val

				if val == '1':
					print "servo1 move pushed %s" % val
				elif val == '2':
					print "servo1 pushed %s" % val
				elif val == '3':
					print "servo1 pushed %s" % val
				elif val == '4':
					print "servo1 pushed %s" % val
				elif val == '5':
					print "servo1 pushed %s" % val

				if val == '6':
					print "servo2 pushed %s" % val
				elif val == '7':
					print "servo2 pushed %s" % val
				elif val == '8':
					print "servo2 pushed %s" % val
				elif val == '9':
					print "servo2 pushed %s" % val
				elif val == '0':
					print "servo2 pushed %s" % val

			except IOError as ex:
				print "I2C Communication Failed %s" % ex

if __name__ == "__main__":
	main()
