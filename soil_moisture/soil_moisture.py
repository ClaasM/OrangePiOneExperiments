import time, signal, sys
from datetime import datetime

import OPi.GPIO as GPIO
import requests

sys.path.append('./SDL_Adafruit_ADS1x15')
# noinspection PyUnresolvedReferences
import SDL_Adafruit_ADS1x15

GPIO.setboard(GPIO.PCPCPLUS)  # ZERO
GPIO.setmode(GPIO.BOARD)

temp_pin = 12
indoor_id = "28-012112f18a66"

ADS1115 = 0x00  # 16-bit ADC
gain = 4096  # +/- 2.048V
sps = 64  # 64 samples per second, works for 3 sensors

# Generous boundaries, s.t. we never exceed 0/100% with a valid reading
water_voltage = 0.8
air_voltage = 2.1
light_voltage = 3.3
dark_voltage = 0

indoor_temp = None

token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJEZXZpY2VDYWxsYmFja19PUGlPbmUiLCJzdnIiOiJldS1jZW50cmFsLmF3cy50aGluZ2VyLmlvIiwidXNyIjoiQ2xhYXNNIn0.hHV6oyIU5asqVi_98wU74TAJT_SLaFHLiLt61j-PRVw"
thinger_url = "https://backend.thinger.io/v3/users/ClaasM/devices/OPiOne/callback/data"

# Only start sending after the program has been running for 10 minutes
last_sent = time.time()
# Initialise the ADC using the default mode (use default I2C address)
adc = SDL_Adafruit_ADS1x15.ADS1x15(ic=ADS1115)
while (1):

    try:
        with open("/sys/bus/w1/devices/%s/w1_slave" % indoor_id, "r") as f:
            data = f.read()
            if "YES" in data:
                (discard, sep, reading) = data.partition(' t=')
                indoor_temp = float(reading) / 1000.0  # reports temperature in degrees C
    except Exception as e:
        print(e)
        pass


    # Read channels  in single-ended mode using the settings above
    voltsCh0 = adc.readADCSingleEnded(0, gain, sps) / 1000  # 1€ plant
    voltsCh1 = adc.readADCSingleEnded(1, gain, sps) / 1000  # Ikea Palme
    voltsCh2 = adc.readADCSingleEnded(2, gain, sps) / 1000  # Lina's present
    voltsCh3 = adc.readADCSingleEnded(3, gain, sps) / 1000  # Light sensor

    # Also possible to use adc.readRaw(0, gain, sps)
    print("Voltages: %.6fV %.6fV %.6fV %.6fV" % (voltsCh0, voltsCh1, voltsCh2, voltsCh3))
    moisture0 = 100 - min(max(voltsCh0 - water_voltage, 0) / (air_voltage - water_voltage), 1) * 100
    moisture1 = 100 - min(max(voltsCh1 - water_voltage, 0) / (air_voltage - water_voltage), 1) * 100
    moisture2 = 100 - min(max(voltsCh2 - water_voltage, 0) / (air_voltage - water_voltage), 1) * 100
    light = min(max(voltsCh3 - dark_voltage, 0) / (light_voltage - dark_voltage), 1) * 100
    print("Moisture: %.2f%% %.2f%% %.2f%% Brightness %.2f%% Temperature %.2f°C" % (moisture0, moisture1, moisture2, light, indoor_temp or -1))

    if time.time() - last_sent > 60 * 10:
        print("Sending Update")
        last_sent = time.time()
        payload = {
            "time": datetime.now().isoformat(),
            "percentage_0": moisture0,
            "percentage_1": moisture1,
            "percentage_2": moisture2,
            "light": light,
            "temperature": indoor_temp,
        }
        try:
            res = requests.post(thinger_url, json=payload, headers={'Authorization': token})
        except Exception as e:
            print(e)
            pass

    time.sleep(1)  # 10 * 60
