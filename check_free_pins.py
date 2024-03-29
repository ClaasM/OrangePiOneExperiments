print("Hello World")
# Blink all Pins that can be set to I/O out


import OPi.GPIO as GPIO  # this was installed by sudo, so
from time import sleep  # this lets us have a time delay

from time import sleep  # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

try:
    working = []
    for i in range(100):
        try:
            GPIO.setup(i, GPIO.OUT)
            working.append(i)
            print(i)
        except ValueError as e:
            print(e)
            pass

    while True:
        for i in working:
            GPIO.output(i, 1)
            print(i)
            print("On")
        sleep(0.5)
        for i in working:
            GPIO.output(i, 0)
            print(i)
            print("Off")

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean GPIO
    print("Bye.")


"""
7
Working
8
Working
10
Working
12
Working
15
Working
16
Working
18
Working
22
Working
26
Working
29
Working
31
Working
32
Working
33
Working
35
Working
36
Working
37
Working

"""