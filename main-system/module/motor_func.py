#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

#import smbus
import time
#import RPi.GPIO as GPIO
from module import *

class MotorSignal:
    direction = FORWARD
    speed = 0

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__limit()

    ''' I2Cで出力する値を取得します．
    @return 8bitに信号をまとめた値
    '''
    def signal(self):
        return (int(self.speed) / 2) << 2 | 0b1 if self.direction == BACKWARD else 0b0

    def __limit(self):
        '''  '''
        if self.speed > 255:
            self.speed = 255
        elif self.speed < 0:
            self.speed = 0

def motor_move( target, *motor_signal ) :
    target.write_data(*[s.signal() for s in motor_signal])
    print "Motor move"
