#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

import pygame
import RPI.GPIO as GPIO
import smbus
import time
from i2c import i2cConnection

ADDRESS_UNO = 0x1
ADDRESS_MOTOR1 = 0x10
ADDRESS_MOTOR2 = 0x11
ADDRESS_SERVO1   = 0x20
ADDRESS_SERVO2   = 0x21

MOTOR_MOVE = 0
MOTOR_MOVE_R = 1
SERVO_MOVE = 2
SERVO_MOVE = 3

# Raspberry pi GPIO setting
def init_gpio() :
	GPIO.setmode( GPIO.BCM )

# Game pad controller initialize
def init_controller() :
	pyngame.joystick.init()
	try :
		joys = pygame.joystick.Joystick(0)
		njoy.init()
		return joys
	except pygame.error :
		print "Not found controller"

if __name__ == "__main__":
	init_gpio()
	con = init_controller()
	
	# I2C initialize
	uno = i2cConnection( ADDRESS_UNO, 1 )
	motor1 = i2cConnection( ADDRESS_MOTOR1, 2 )
	motor2 = i2cConnection( ADDRESS_MOTOR2, 3 )
	servo1 = i2cConnection( ADDRESS_SERVO1, 4 )
	servo2 = i2cConnection( ADDRESS_SERVO2, 5 )

	# Main systm loop
	while True :
		time.sleep( 0.1 )
		try :
			# Get controller event
			for e in pygame.event.get() :
				# Button pressed
				if e.type == pygame.locals.JOYBUTTONDOWN:
					# Motor move
					if e.button == MOTOR_MOVE :
						print "MOTOR MOVE"
					if e.button == MOTOR_MOVE_R :
						print "MOTOR MOVE R"

		except IOError as ex :
			print "I2C Communication Failed %s" % ex
