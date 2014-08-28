#!/usr/bin/python
# encoding: utf-8

import RPi.GPIO as GPIO
from module import *
from settings import *
from module.i2c_class import *
from module import motor_func
from module.motor_func import MotorSignal
from module import servo_func
import logging
import math

# 一列アームの前後モータの値
forth_back_motor_signal = MotorSignal()

# 一列アームの上下モータの値
up_down_motor_signal = MotorSignal()

# 一列ハンドのサーボ角度
line_hand_servo = LINE_HAND_RELEASE_ANGLE

# 特攻ハンドのサーボの角度
suicide_hand_servo = SUICIDE_HAND_RELEASE_ANGLE

# 特攻ハンドの展開収縮サーボ角度
suicide_arm_servo = SUICIDE_ARM_RETURN_ANGLE

# I2C initialize
motor1 = I2CConnect( I2C_ADDRESS['MOTOR1'] )
servo1 = I2CConnect( I2C_ADDRESS['SERVO1'] )
air = I2CConnect( I2C_ADDRESS['AIR'] )
modules = {'motor1': motor1, 'servo1': servo1, 'air': air}
logging.info("Initialize I2C communication to modules [OK]")

''' 特攻ハンドを閉じてつかみます '''
def catch_suicide_hand():
    global suicide_hand_servo
    suicide_hand_servo = SUICIDE_HAND_CATCH_ANGLE
    __send_servo1_signal()

''' 特攻ハンドを開きます '''
def release_suicide_hand():
    global suicide_hand_servo
    suicide_hand_servo = SUICIDE_HAND_RELEASE_ANGLE
    __send_servo1_signal()

''' 一列ハンドを閉じてつかみます '''
def catch_line_hand():
    global line_hand_servo
    line_hand_servo = LINE_HAND_CATCH_ANGLE
    __send_servo1_signal()

''' 一列ハンドを開きます '''
def release_line_hand():
    global line_hand_servo
    line_hand_servo = LINE_HAND_RELEASE_ANGLE
    __send_servo1_signal()

''' 特攻アームを展開します '''
def expand_suicide_arm():
    global suicide_arm_servo
    suicide_arm_servo = SUICIDE_ARM_EXPAND_ANGLE
    __send_servo1_signal()

''' 特攻アームを収縮します '''
def return_suicide_arm():
    global suicide_arm_servo
    suicide_arm_servo = SUICIDE_ARM_RETURN_ANGLE
    __send_servo1_signal()

''' 一列アームを前後移動します． '''
def act_line_arm_forth_back(stick_val):
    if __is_valid_stick(stick_val):
        forth_back_motor_signal.speed = math.fabs(stick_val) * 255
        forth_back_motor_signal.direction = FORWARD if stick_val < 0 else BACKWARD
    else:
        forth_back_motor_signal.speed = 0
        forth_back_motor_signal.direction = FORWARD
    print "fb %d, %d" % (forth_back_motor_signal.direction, forth_back_motor_signal.speed)
    __send_motor_signal()

''' 一列アームの上下移動をします '''
def act_line_arm_up_down(stick_val):
    if __is_valid_stick(stick_val):
        up_down_motor_signal.speed = math.fabs(stick_val) * 255
        up_down_motor_signal.direction = FORWARD if stick_val < 0 else BACKWARD
    else:
        up_down_motor_signal.speed = 0
        up_down_motor_signal.direction = FORWARD
    print "up %d, %d" % (up_down_motor_signal.direction, up_down_motor_signal.speed)
    __send_motor_signal()

''' モータシグナルを送信します． '''
def __send_motor_signal():
    global  forth_back_motor_signal, up_down_motor_signal
    modules['motor1'].write_data(forth_back_motor_signal.signal(), up_down_motor_signal.signal())

''' スティックの傾きが遊びの範囲内かどうかを判定します．
@param stick_val スティックの入力値
@return True: 有効な角度, False: 遊びの範囲内(無効)
'''
def __is_valid_stick(stick_val):
    if stick_val > -1 * JOYSTICK_BACKLASH and stick_val < JOYSTICK_BACKLASH:
        return False
    else:
        return True

''' エアシリンダを開きます '''
def open_air_cylinder():
    modules['air'].write_data(0x01)

''' エアシリンダを閉じます '''
def close_air_cylinder():
    modules['air'].write_data(0x00)

''' GPIOピンのエアシリンダを開きます． '''
def open_air_cylinder_gpio():
    GPIO.output(GPIO_AIR_CYLINDER, GPIO.HIGH)

''' GPIOピンのエアシリンダを閉じます． '''
def close_air_cylinder_gpio():
    GPIO.output(GPIO_AIR_CYLINDER, GPIO.LOW)

''' ハンド，アーム系のサーボにデータを送信します '''
def __send_servo1_signal():
    servo_func.move(modules['servo1'], line_hand_servo, suicide_hand_servo, suicide_arm_servo)

''' ハードウェアを初期位置にします '''
def init_hardware():
    global forth_back_motor_signal, up_down_motor_signal
    global line_hand_servo, suicide_hand_servo, suicide_arm_servo
    global air_cylinder_expand_servo, air_cylinder_oc_servo
    forth_back_motor_signal = MotorSignal()
    up_down_motor_signal = MotorSignal()
    line_hand_servo = LINE_HAND_RELEASE_ANGLE
    suicide_hand_servo = SUICIDE_HAND_RELEASE_ANGLE
    suicide_arm_servo = SUICIDE_ARM_RETURN_ANGLE
    __send_motor_signal()
    __send_servo1_signal()
    modules['air'].write_data(0x00)

def retry():
    pass

''' 緊急事態停止ボタンが押されているかどうかを取得します．
@return True: 平常, False: 緊急事態
'''
def is_emergency():
    return not GPIO.input(GPIO_EMERGENCY)