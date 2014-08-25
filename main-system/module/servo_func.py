#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

import smbus
import time
import RPi.GPIO as GPIO

# Parameter limit function
def limit( param ) :
	if param > 180 :
		return 180
	elif param < 0 :
		return 0
	else :
		return int(param)

def move( target, *angle ) :
	target.write_data( *[limit(a) for a in angle] )

def test() :
	print "test"
