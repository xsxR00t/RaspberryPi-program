#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
import smbus
import time
import test_mo

ADDRESS_UNO = 0x1
ADDRESS_MOTOR1 = 0x10
ADDRESS_MOTOR2 = 0x11
ADDRESS_SERVO1   = 0x20
ADDRESS_SERVO2   = 0x21

MOTOR_MOVE = 0
MOTOR_MOVE_R = 1
SERVO_MOVE = 2
SERVO_MOVE = 3

test_press = None

# Raspberry pi GPIO setting
def init_gpio() :
	GPIO.setmode( GPIO.BCM )

# Game pad controller initialize
def init_controller() :
p	pygame.joystick.init()
	try :
		joys = pygame.joystick.Joystick(0)
		joys.init()
		pygame.init()
		print "Game pad initialized"
		return joys
	except pygame.error :
		print "Not found controller"
		quit()

if __name__ == "__main__":
	init_gpio()
	con = init_controller()

	'''
	# I2C initialize
	uno = i2cConnection( ADDRESS_UNO, 1 )
	motor1 = i2cConnection( ADDRESS_MOTOR1, 2 )
	motor2 = i2cConnection( ADDRESS_MOTOR2, 3 )
	servo1 = i2cConnection( ADDRESS_SERVO1, 4 )
	servo2 = i2cConnection( ADDRESS_SERVO2, 5 )
	'''

	# Main systm loop
	while True :
		time.sleep( 0.1 )
		try :
			# Get controller event
			for e in pygame.event.get() :
				# Button pressed
				if e.type == pygame.locals.JOYBUTTONDOWN :
					# Motor move
					if e.button == MOTOR_MOVE :
						print "MOTOR MOVE"
					if e.button == MOTOR_MOVE_R :
						print "MOTOR MOVE R"
					test_press = e.button
				# Button released
				elif e.type == pygame.locals.JOYBUTTONUP :
					if e.button == MOTOR_MOVE :
						print "MOTOR STOP"
					test_press = e.button*(-1)+(-1)

				# Analog stick
				# h_axis_pos = con.get_axis(0)
				# v_axis_pos = con.get_axis(1)
				# print (h_axis_pos, v_axis_pos)
			if test_press == MOTOR_MOVE :
				print "MOTOR MOVE"
			elif test_press == -1 :
				print "MOTOR STOP"
			print test_press

		except IOError as ex :
			print "I2C Communication Failed %s" % ex
