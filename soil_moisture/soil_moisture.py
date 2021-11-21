import time, signal, sys
from datetime import datetime

import requests

sys.path.append('./SDL_Adafruit_ADS1x15')
# noinspection PyUnresolvedReferences
import SDL_Adafruit_ADS1x15

ADS1115 = 0x00  # 16-bit ADC
gain = 2048  # +/- 2.048V
sps = 64  # 64 samples per second, works for 3 sensors

# Generous boundaries, s.t. we never exceed 0/100% with a valid reading
water_voltage = 0.8
air_voltage = 2.1

token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJEZXZpY2VDYWxsYmFja19PUGlPbmUiLCJzdnIiOiJldS1jZW50cmFsLmF3cy50aGluZ2VyLmlvIiwidXNyIjoiQ2xhYXNNIn0.hHV6oyIU5asqVi_98wU74TAJT_SLaFHLiLt61j-PRVw"
thinger_url = "https://backend.thinger.io/v3/users/ClaasM/devices/OPiOne/callback/data"

last_sent = None
# Initialise the ADC using the default mode (use default I2C address)
adc = SDL_Adafruit_ADS1x15.ADS1x15(ic=ADS1115)
while (1):
    # Read channels  in single-ended mode using the settings above
    voltsCh0 = adc.readADCSingleEnded(0, gain, sps) / 1000  # 1€ plant
    voltsCh1 = adc.readADCSingleEnded(1, gain, sps) / 1000  # Ikea Palme
    voltsCh2 = adc.readADCSingleEnded(2, gain, sps) / 1000  # Lina's present
    # Also possible to use adc.readRaw(0, gain, sps)
    print("Voltages: %.6fV %.6fV %.6fV" % (voltsCh0, voltsCh1, voltsCh2))
    moisture0 = 100 - min(max(voltsCh0 - water_voltage, 0) / (air_voltage - water_voltage), 1) * 100
    moisture1 = 100 - min(max(voltsCh1 - water_voltage, 0) / (air_voltage - water_voltage), 1) * 100
    moisture2 = 100 - min(max(voltsCh2 - water_voltage, 0) / (air_voltage - water_voltage), 1) * 100
    print("Moisture: %.2f%% %.2f%% %.2f%%" % (moisture0, moisture1, moisture2))

    if last_sent is None or time.time() - last_sent > 60 * 10:
        print("Sending Update")
        last_sent = time.time()
        payload = {
            "time": datetime.now().isoformat(),
            "percentage_0": moisture0,
            "percentage_1": moisture1,
            "percentage_2": moisture2
        }
        try:
            res = requests.post(thinger_url, json=payload, headers={'Authorization': token})
        except Exception as e:
            print(e)
            pass

    time.sleep(1)  # 10 * 60
