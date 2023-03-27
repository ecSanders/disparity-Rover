import time
import sys
sys.path.append('/home/pi/env/lib/python3.9/site-packages')
# Found out that the package is only going to work on Raspberrypi
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
turnleft = 3
turnright = 5
# GPIO pins
# 11 13 15 16
FwdLeftBack = 11
ReversLeftBack = 13
FwdRightBack = 15
ReversRightBack = 16

#Front Stearing
GPIO.setup(turnleft, GPIO.OUT)
GPIO.setup(turnright, GPIO.OUT)

GPIO.setup(FwdLeftBack, GPIO.OUT)
GPIO.setup(FwdRightBack, GPIO.OUT)
GPIO.setup(ReversLeftBack, GPIO.OUT)
GPIO.setup(ReversRightBack, GPIO.OUT)
time.sleep(30)

#Front Moter

GPIO.setup(turnleft, GPIO.HIGH)
GPIO.setup(turnleft, GPIO.HIGH)
time.sleep(1)
GPIO.setup(turnleft, GPIO.LOW)
GPIO.setup(turnleft, GPIO.LOW)
time.sleep(1)


# Back moters

GPIO.setup(FwdLeftBack, GPIO.HIGH)
GPIO.setup(FwdRightBack, GPIO.HIGH)
GPIO.setup(ReversLeftBack, GPIO.HIGH)
GPIO.setup(ReversRightBack, GPIO.HIGH)
time.sleep(1)
GPIO.setup(FwdLeftBack, GPIO.LOW)
GPIO.setup(FwdRightBack, GPIO.LOW)
GPIO.setup(ReversLeftBack, GPIO.LOW)
GPIO.setup(ReversRightBack, GPIO.LOW)
time.sleep(1)

GPIO.cleanup()