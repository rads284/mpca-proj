import RPi.GPIO as GPIO
import time
from test import testfun
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
from picamera import PiCamera
from time import sleep

camera = PiCamera()
try:
     while True:
            input_state=GPIO.input(11)
            if input_state == False:
                for i in range(1,6):
                    sleep(3)
                    camera.capture('test-data/test%s.jpg' % i)
                # testfun()
except KeyboardInterrupt:
     GPIO.cleanup()
