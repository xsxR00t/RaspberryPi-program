#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

import smbus
import time
import RPI.GPIO as GPIO
from i2c import i2cConnection

# Parameter limit function
def limit( param ) :
	if param > 180 :
		return 180
	elif param < 0 :
		return 0
	else :
		return param

def servo_move( target, angle ) :
	target.write( limit( angle ) )
	
def servo_move_r( target, angle ) :
	target.write( limit( angle ) )
