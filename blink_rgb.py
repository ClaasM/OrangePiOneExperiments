import OPi.GPIO as GPIO  # this was installed by sudo, so

from time import sleep  # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

# GPIO usable Pins are: 3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,27,28,29,31,32,33,35,36,337,38,40
R_PIN = 33
G_PIN = 35
B_PIN = 37
period = 0.5

GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)

try:
    while True:
        sleep(period)
        GPIO.output(R_PIN, 0)
        GPIO.output(G_PIN, 1)
        sleep(period)
        GPIO.output(G_PIN, 0)
        GPIO.output(B_PIN, 1)
        sleep(period)
        GPIO.output(B_PIN, 0)
        GPIO.output(R_PIN, 1)
except KeyboardInterrupt:
    GPIO.output(R_PIN, 0)  # set port/pin value to 0/LOW/False
    GPIO.cleanup()  # Clean GPIO
    print("Bye.")
