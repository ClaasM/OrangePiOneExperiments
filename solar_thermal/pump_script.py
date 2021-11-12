# noinspection PyUnresolvedReferences
import math
import time
from datetime import datetime
from time import sleep

import OPi.GPIO as GPIO
import requests

GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

PIN = 3

GPIO.setup(PIN, GPIO.OUT)

# TODO add warning if script older than x seconds s.t. we notice if upload didn't work
t = 20

print("Pumping")
GPIO.output(PIN, 1)
sleep(t)
print("Not Pumping")
GPIO.output(PIN, 0)
