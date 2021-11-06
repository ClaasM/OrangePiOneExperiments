print("Hello World")
# Using a DSB18B20, following this tutorial: https://blog.ja-ke.tech/2019/01/21/DS18B20-armbian.html

import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    print("The temperature is %s celsius" % temperature)
    time.sleep(1)