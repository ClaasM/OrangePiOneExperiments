# noinspection PyUnresolvedReferences
from time import sleep  # this lets us have a time delay

import OPi.GPIO as GPIO  # this was installed by sudo, so
# noinspection PyUnresolvedReferences
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

PIN = 3
period = 1

GPIO.setup(PIN, GPIO.OUT)

# TODO add warning if script older than x seconds s.t. we notice if upload didn't work

try:
    while True:
        temperature = sensor.get_temperature()
        print("The temperature is %s celsius" % temperature)
        if temperature > 10:
            print("Pumping")
            GPIO.output(PIN, 1)
        else:
            print("Not pumping")
            GPIO.output(PIN, 0)
        sleep(period)
except KeyboardInterrupt:
    GPIO.output(PIN, 0)  # set port/pin value to 0/LOW/False
    GPIO.cleanup()  # Clean GPIO
    print("Bye.")
