#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

from daemon import daemon
from daemon.pidlockfile import PIDLockFile
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
import smbus
import time
import logging

# User program
from module.motor_func import *
from module.i2c_class import I2CConnect

PID_FILE = '/var/run/catchrobot.pid'

ADDRESS_UNO = 0x01
ADDRESS_MOTOR1 = 0x10
ADDRESS_MOTOR2 = 0x11
ADDRESS_SERVO1   = 0x20
ADDRESS_SERVO2   = 0x21

MOTOR_MOVE = 0
MOTOR_MOVE_R = 1
SERVO_MOVE = 2
SERVO_MOVE = 3

modules = {}

# Raspberry pi GPIO setting
def init_gpio() :
    GPIO.setmode( GPIO.BCM )

# Game pad controller initialize
def init_controller() :
    pygame.joystick.init()
    try :
        joys = pygame.joystick.Joystick(0)
        joys.init()
        pygame.init()
        print "Controller initialized"
        return joys
    except pygame.error :
        print "Not found controller"
        quit()

def main_routine( cmd ) :
    # Motor wake
    if cmd == MOTOR_MOVE :
        print "motor moving"
        motor_move( modules['motor1'], 100, 100, 100 )
        time.sleep(0.1)
        print modules['motor1'].read_data(3)
    elif cmd == MOTOR_MOVE*(-1)+(-1) :
        motor_move_r(0,0)
    else :
        print "Motor stop"

    # Servo wake

def main():
    init_gpio()
    con = init_controller()

    # I2C initialize
    # uno = I2CConnect(ADDRESS_UNO)
    motor1 = I2CConnect( ADDRESS_MOTOR1 )
    # motor2 = i2cConnection( ADDRESS_MOTOR2, 3 )
    # servo1 = i2cConnection( ADDRESS_SERVO1, 4 )
    # servo2 = i2cConnection( ADDRESS_SERVO2, 5 )
    modules.update({'motor1': motor1})
    logging.info("Initialize I2C communication to modules [OK]")

    # Receive controller keys
    getCommand = None

    # Main systm loop
    while True :
        time.sleep( 0.1 )
        try :
            # Get controller event
            for e in pygame.event.get() :
                # Button pressed
                if e.type == pygame.locals.JOYBUTTONDOWN :
                    getCommand = e.button
                # Button released
                elif e.type == pygame.locals.JOYBUTTONUP :
                    getCommand = e.button*(-1)+(-1)

            # Main routine
            main_routine( getCommand )

        except IOError as ex :
            str = "I2C Communication Failed %s" % ex
            logging.error(str)
            print str

if __name__ == "__main__":
    #with daemon.DaemonContext(pidfile=PIDLockFile(PID_FILE)):
    main()