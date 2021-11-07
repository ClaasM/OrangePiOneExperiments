# noinspection PyUnresolvedReferences
import OPi.GPIO as GPIO  # this was installed by sudo, so
import os

from time import sleep  # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

PIN = 3
period = 2

GPIO.setup(PIN, GPIO.OUT)
#os.system('echo 12 > /sys/class/gpio/export')
#os.system('echo out > /sys/class/gpio/gpio12/direction')

try:
    while True:
        print("Turning on pin %d" % PIN)
        #os.system('echo 1 > /sys/class/gpio/gpio12/value')
        GPIO.output(PIN, 1)
        sleep(period)
        #os.system('echo 0 > /sys/class/gpio/gpio12/value')
        GPIO.output(PIN, 0)
        sleep(period)
except KeyboardInterrupt:
    os.system('echo 12 > /sys/class/gpio/unexport')
    GPIO.output(PIN, 0)  # set port/pin value to 0/LOW/False
    GPIO.cleanup()  # Clean GPIO
    print("Bye.")
