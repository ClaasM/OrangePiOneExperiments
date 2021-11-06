import OPi.GPIO as GPIO  # this was installed by sudo, so

from time import sleep  # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

R_PIN = 33
G_PIN = 35
B_PIN = 37
period = 0.5

GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)

try:
    while True:
        # RGB mixing doesn't really work with this LED
        sleep(period)
        #GPIO.output(R_PIN, 0)
        GPIO.output(G_PIN, 1)
        sleep(period)
        #GPIO.output(G_PIN, 0)
        GPIO.output(B_PIN, 1)
        sleep(period)
        #GPIO.output(B_PIN, 0)
        GPIO.output(R_PIN, 1)
except KeyboardInterrupt:
    GPIO.output(R_PIN, 0)  # set port/pin value to 0/LOW/False
    GPIO.cleanup()  # Clean GPIO
    print("Bye.")
