#!/usr/bin/python

import subprocess
import sys
import time

terminal=["screen /dev/tty.raspberrypi-SerialPort 9600"]
workingDirectory="/home/pi/Eyes-On/python/examples"
# test= 'ls'
# tester= str.encode(test)
#type(tester)x

pi = subprocess.Popen(terminal, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
(out, err) = pi.communicate()
print(out)
