# noinspection PyUnresolvedReferences
import OPi.GPIO as GPIO  # this was installed by sudo, so

from time import sleep  # this lets us have a time delay

from Adafruit_Python_DHT import Adafruit_DHT

GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

clk = 18
dt = 16
# TODO learning: you can't actually use any pin, they have to be PC/PA pins
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        # print(dtState, clkState)
        if clkState != clkLastState:
            if dtState != clkState:
                counter += 1
            else:
                counter -= 1
            print(counter)
        clkLastState = clkState
        sleep(0.001)  # If we sleep too long we skip steps when turning fast
finally:
    GPIO.cleanup()
