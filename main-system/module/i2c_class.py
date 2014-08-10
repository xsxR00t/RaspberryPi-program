#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

import smbus

class I2CConnect :
	bus = smbus.SMBus(1)

	def __init__( self, address ) :
		# Target address
		self.address = address

	def writeDate( self, data ) :
		self.bus.write_byte( self.address, data )
		print "Write!"

	def readDate( self ) :
		return self.bus.read_byte( self.address )

	def test( self ) :
		print "get"
