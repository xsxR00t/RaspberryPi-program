#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi

import sys
from subprocess import *

wakeProgram = 'gpioTest.py'

pid = Popen( ['sudo', 'python', wakeProgram, '&'] ).pid
print pid
