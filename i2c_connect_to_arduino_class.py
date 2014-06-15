#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

import smbus
import time

class I2cConnects:
	bus = smbus.SMBus(1)

	def __init__(self, address):
		# Target address
		self.address = address

	def writeData(self, data):
		self.bus.write_byte( self.address, data )

	def readData(self):
		return self.bus.read_byte( self.address )

def main():
	i2cList = []
	i2cList.append( I2cConnects(0x0a) )
	i2cList.append( I2cConnects(0x0c) )

	while True:
		for slave in i2cList:
			var = input("Enter number (to slave address(" + hex(slave.address) + ") :")
			if not var:
				continue
			
			# Send data
			slave.writeData( var )
			print "RPI -> arduino(" + hex(slave.address) + " : %d" % var
			time.sleep(1)

			# Read data
			print "Arduino(" + hex(slave.address) + ") -> RPI : %d" % slave.readData()
			print
			

if __name__ == '__main__':
	main()
