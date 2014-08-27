#!/usr/bin/python
# encoding: utf-8

''' 緊急停止スイッチが押されたときの例外 '''
class EmergencyException(Exception):
    def __init__(self):
        super(Exception).__init__(self)
