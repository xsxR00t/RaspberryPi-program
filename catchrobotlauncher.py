#!/usr/bin/python
#encoding: utf-8

from daemon import daemon
from daemon.pidlockfile import PIDLockFile
import RPi.GPIO as GPIO
import subprocess
import os
import time
import logging

PID_FILE = '/var/run/catchrobotlauncher.pid'
PROCESS = '/home/pi/src/RaspberryPi-program/main-system/main.py'
GPIO_EMERGENCY = 9

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_EMERGENCY, GPIO.IN)
    running = False
    pid = -1

    while True:
        time.sleep(0.1)
        pin = GPIO.input(GPIO_EMERGENCY)
        if pin and running is False:
            pid = subprocess.Popen(['sudo', 'python', PROCESS]).pid
            running = True
            print "launched %s" % pid
            logging.info("%s is launch at %s" % PROCESS, pid)
        elif pin is False and running is True:
            os.kill(pid)
            running = False
            print "killed"
            logging.info("%s is killed" % PROCESS)

if __name__ == '__main__':
    #with daemon.DaemonContext(pidfile=PIDLockFile(PID_FILE)):
    main()