# noinspection PyUnresolvedReferences
import math
import time
from datetime import datetime

import OPi.GPIO as GPIO
import requests

GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

PIN = 3
period = 15

GPIO.setup(PIN, GPIO.OUT)

# TODO add warning if script older than x seconds s.t. we notice if upload didn't work

token = "Bearer add_token"
thinger_url = "https://backend.thinger.io/v3/users/ClaasM/devices/OPiZero/callback/data"

last_measurements = []

try:
    while True:
        starttime = time.time()
        outdoor_id = "28-012112f84728"
        indoor_id = "28-012112f18a66"
        outdoor_temp = None
        indoor_temp = None
        watts = 0

        try:
            with open("/sys/bus/w1/devices/%s/w1_slave" % outdoor_id, "r") as f:
                data = f.read()
                if "YES" in data:
                    (discard, sep, reading) = data.partition(' t=')
                    outdoor_temp = float(reading) / 1000.0  # reports temperature in degrees C
        except Exception as e:
            print(e)
            pass

        try:
            with open("/sys/bus/w1/devices/%s/w1_slave" % indoor_id, "r") as f:
                data = f.read()
                if "YES" in data:
                    (discard, sep, reading) = data.partition(' t=')
                    indoor_temp = float(reading) / 1000.0  # reports temperature in degrees C
        except Exception as e:
            print(e)
            pass

        if outdoor_temp is not None and indoor_temp is not None:
            print("Got valid reading. Indoor %.4f, outdoor %.4f - " % (indoor_temp, outdoor_temp), end="")

            # Compute wattage
            last_measurements.append(indoor_temp)
            if len(last_measurements) == 50:
                latest_5 = last_measurements[25:]
                earlier_5 = last_measurements[:25]
                avg_before = sum(earlier_5) / 25.0
                avg_after = sum(latest_5) / 25.0
                t = 5.0 * period
                calories = (avg_after - avg_before) * 60000.0  # milliliter in
                watt_hours = calories * 0.00116222
                watts = watt_hours / t * 60.0 * 60.0
                print("%.4f Watts - " % watts, end="")
                last_measurements.pop(0)
            else:
                print("Not enough measurements for wattage - ", end="")

            # Turn on pump on 5 degree threshold, but only turn it off after passing 3 degree threshold
            if indoor_temp + 5 < outdoor_temp:
                print("Pumping")
                GPIO.output(PIN, 1)
            elif indoor_temp + 3 > outdoor_temp:
                print("Not Pumping")
                GPIO.output(PIN, 0)
            else:
                pass
                print("Doing Nothing")

            # Probably moving the sensor
            if abs(watts) > 2000:
                watts = 0

            payload = {
                "time": datetime.now().isoformat(),
                "outdoor_temp": outdoor_temp,
                "indoor_temp": indoor_temp,
                "watts": watts,
            }
            try:
                res = requests.post(thinger_url, json=payload, headers={'Authorization': token})
            except Exception as e:
                print(e)
                pass

        # sleep rest of period
        sleep_for = period - (time.time() - starttime)
        time.sleep(max(sleep_for, 0))

except KeyboardInterrupt:
    GPIO.output(PIN, 0)  # set port/pin value to 0/LOW/False
    GPIO.cleanup()  # Clean GPIO
    print("Bye.")
