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
	cnt1 = I2cConnects(0x0a)
	cnt2 = I2cConnects(0x0c)

	while True:
		var = input("Enter number1 : ")
		if not var:
			continue

		var2 = input("Enter number2 : ")
		if not var2:
			continue

		# Send data
		cnt1.writeData(var)
		cnt2.writeData(var2)
		print "RPI -> arduino(%d) : %d" % (cnt1.address, var)
		print "RPI -> arduino(%d) : %d" % (cnt2.address, var2)
		time.sleep(1)

		# Read data
		print "Arduino(%d) -> RPI : %d" % (cnt1.address, cnt1.readData())
		print "Arduino(%d) -> RPI : %d" % (cnt2.address, cnt2.readData())
		print

if __name__ == '__main__':
	main()
