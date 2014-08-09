#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

import smbus
import time
import RPI.GPIO as GPIO
from i2c import i2cConnection

# Parameter limit function
def limit( param ) :
	if param > 255 :
		return 255
	elif param < 0 :
		return 0
	else :
		return param

def motor_move( target, speed ) :
	target.write( limit( speed ) )

def motor_move_r( target, speed ) :
	target.write( limit( speed ) )
