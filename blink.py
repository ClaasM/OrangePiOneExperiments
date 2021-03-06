import OPi.GPIO as GPIO  # this was installed by sudo, so

from time import sleep  # this lets us have a time delay

GPIO.setboard(GPIO.ZERO)  # ZERO
GPIO.setmode(GPIO.BOARD)

# Usable Pins on the Zero: 7, 12, 15, ...
pin = 15
period = 0.5

GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        GPIO.output(pin, 1)  # set port/pin value to 1/HIGH/True
        sleep(period)
        GPIO.output(pin, 0)  # set port/pin value to 1/HIGH/True
        sleep(period)
except KeyboardInterrupt:
    GPIO.output(pin, 0)  # set port/pin value to 0/LOW/False
    GPIO.cleanup()  # Clean GPIO
    print("Bye.")
