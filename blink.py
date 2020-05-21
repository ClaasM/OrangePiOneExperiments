import OPi.GPIO as GPIO  # this was installed by sudo, so

from time import sleep  # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

# GPIO usable Pins are: 3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,27,28,29,31,32,33,35,36,337,38,40
pin = 3
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
