#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

import smbus
import time

# RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)
# Arduino address
address = 0x0a

def writeNumber(data):
	bus.write_byte( address, data )
	#bus.write_byte_data( address, 0, data )
	return -1

def readNumber():
	number = bus.read_byte( address )
	# number = bus.read_byte_data( address, 1 )
	return number

def main():
	while True:
		var = input("Enter 1 - 9: ")
		# not input number
		if not var:
			continue

		# Send data
		writeNumber(var)
		print "RPI -> arduino : ", var
		# sleep one second
		time.sleep(1)

		# Read data
		number = readNumber()
		print "Arduion -> RPI ", number
		print

if __name__ == "__main__":
	main()
