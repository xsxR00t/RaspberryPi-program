#!/usr/bin/python
# encoding: utf-8

import pygame
from pygame.locals import *
import time
import RPi.GPIO as GPIO
import smbus
from i2c import I2cConnection

I2C_UNO = 0x1
I2C_MOTOR1 = 0x10
I2C_MOTOR2 = 0x11
I2C_SERVO1 = 0x20
I2C_SERVO2 = 0x21

def initIO():
    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(17, GPIO.OUT)
#    GPIO.setup(22, GPIO.OUT)
#    GPIO.setup(27, GPIO.OUT)
#   GPIO.output(17, True)
#    GPIO.output(22, True)
#    GPIO.output(27, True)

def main():
    initIO()
#    joys = pygame.joystick.Joystick(0)
#    joys.init()
    pygame.init()

    motor1 = I2cConnection(I2C_MOTOR1,1)
    motor2 = I2cConnection(I2C_MOTOR2,2)
    servo1 = I2cConnection(I2C_SERVO1,3)
    servo2 = I2cConnection(I2C_SERVO2,4)

    print "initialized"
    while True:
        time.sleep(0.1)
#        for e in pygame.event.get():
        while True:
            time.sleep(0.1)
            try:
#                if e.type == pygame.KEYDOWN:
                if True:
                    pressed_keys = pygame.key.get_pressed()
                    val = raw_input("Enter:")
                    print val
                    if val == 'a':
                        print "pushed %s" % val
                        move_motor(motor1, 255)
                    elif val == 's':
                        print "motor1 stop"
                        move_motor(motor1, 0)

                    if val == 'b':
                        print "pushed %s" % val
                        move_motor(motor2, 255)
                    elif val == 'v':
                        move_motor(motor2, 0)

                    if val == '1':
                        print "servo1 move pushed %s" % val
                        move_servo(servo1, 5)
                    elif val == '2':
                        print "servo1 pushed %s" % val
                        move_servo(servo1, 45)
                    elif val == '3':
                        print "servo1 pushed %s" % val
                        move_servo(servo1, 90)
                    elif val == '4':
                        print "servo1 pushed %s" % val
                        move_servo(servo1, 135)
                    elif val == '5':
                        print "servo1 pushed %s" % val
                        move_servo(servo1, 175)

                    if val == '6':
                        print "servo2 pushed %s" % val
                        move_servo(servo2, 0)
                    elif val == '7':
                        print "servo2 pushed %s" % val
                        move_servo(servo2, 45)
                    elif val == '8':
                        print "servo2 pushed %s" % val
                        move_servo(servo2, 90)
                    elif val == '9':
                        print "servo2 pushed %s" % val
                        move_servo(servo2, 135)
                    elif val == '0':
                        print "servo2 pushed %s" % val
                        move_servo(servo2, 180)
                '''
                if e.type == pygame.locals.JOYBUTTONDOWN:
                    print "%s is pushed"  % e.button
                    if e.button == 0:
                        motor_move(motor1, 255)
                    elif e.button == 1:
                        motor_move(motor2, 255)
                    elif e.type == pygame.locals.JOYBUTTONUP:
                        print "%s is released" % e.button
                        if e.button == 0:
                            motor_move(motor1, 0)
                        elif e.button == 1:
                            motor_move(motor2, 0)
                        elif e.type == pygame.locals.JOYAXISMOTION:
                            axis_values = [joys.get_axis(i) for i in range(4)]
                            move_servo(servo1, axis_values[0])
                            move_servo(servo2, axis_values[2])
               '''
            except IOError as ex:
                print "I2C Communication Failed %s" % ex

def move_motor(motor, speed):
    if speed > 255:
        speed = 255
    elif 255 < 0:
        speed = 0
    motor.write(speed)
    motor.write(speed)

def move_servo(servo, angle):
    if angle > 180:
        angle = 180
    elif angle < 0:
        angle = 0
#    servo.write_block([angle, angle angle])
    servo.write(angle)
    time.sleep(0.1)
    servo.write(angle)
    time.sleep(0.1)
    servo.write(angle)

if __name__ == '__main__':
    pygame.joystick.init()
    main()
