#!/usr/bin/python
# encoding: utf-8

PID_FILE = '/var/run/catchrobot.pid'

I2C_ADDRESS = {
    'MOTOR1': 0x10,
    'SERVO1': 0x20,
    'SERVO2': 0x21,
}

JOYSTICK_NUMBER = 0

''' ゲームパッドのボタン割り当て '''
PAD_BUTTON = {
    'LINE_HAND_OC': 4,
    'SUICIDE_HAND_OC': 5,
    'INITIALIZE': 11,
    'RETRY': 10
}

''' ゲームパッドの十字キー割り当て '''
PAD_HAT = {
    'AIR_CYLINDER_TURN': 0,
    'AIR_CYLINDER_OC': 1,
}

''' ゲームパッドのスティック割り当て '''
PAD_AXIS = {
    'LINE_ARM_BACK_FORTH': 0,
    'LINE_ARM_UP_DOWN': 3
}

AIR_CYLINDER_MODULE_ANGLE_UNIT = 20

''' エアシリンダが開いたときのサーボ角度 '''
AIR_CYLINDER_OPEN_ANGLE = 160

''' エアシリンダが閉じてるときのサーボ角度 '''
AIR_CYLINDER_CLOSE_ANGLE = 35

''' 特攻ハンドがつかんでいるのサーボ角度 '''
SUICIDE_HAND_CATCH_ANGLE = 160

''' 特攻ハンドの普段のサーボ角度 '''
SUICIDE_HAND_RELEASE_ANGLE = 35

''' 特攻アームが展開しているときのサーボ角度 '''
SUICIDE_ARM_EXPAND_ANGLE = 160

''' 特攻アームが収縮しているときのサーボ角度 '''
SUICIDE_ARM_RETURN_ANGLE = 30

''' 一列ハンドがつかんでいるときのサーボ角度 '''
LINE_HAND_CATCH_ANGLE = 160

''' 一列ハンドの普段のサーボ角度 '''
LINE_HAND_RELEASE_ANGLE = 30

''' ジョイスティックの遊びの角度(0.0から1.0) '''
JOYSTICK_BACKLASH = 0.2