# noinspection PyUnresolvedReferences
import OPi.GPIO as GPIO  # this was installed by sudo, so

from time import sleep  # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

clk = 18
dt = 16
R_PIN = 33
G_PIN = 35
B_PIN = 37

GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)

GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

currentLed = R_PIN
GPIO.output(currentLed, 1)

try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                counter += 1
            else:
                counter -= 1
            print(counter)
            if counter % 3 == 0:
                # Turn on red LED
                GPIO.output(currentLed, 0)
                currentLed = R_PIN
                GPIO.output(currentLed, 1)
            elif counter % 3 == 1:
                # Turn on green LED
                GPIO.output(currentLed, 0)
                currentLed = G_PIN
                GPIO.output(currentLed, 1)
            elif counter % 3 == 2:
                # Turn on blue LED
                GPIO.output(currentLed, 0)
                currentLed = B_PIN
                GPIO.output(currentLed, 1)
        clkLastState = clkState
        sleep(0.001)  # If we sleep too long we skip steps when turning fast
finally:
    GPIO.cleanup()
