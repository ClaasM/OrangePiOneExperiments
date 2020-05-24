from flask import Flask

from mpu import get_temperature

app = Flask(__name__)

# sudo nano /etc/rc.local
# sudo python3 /home/orangepi/OPiOneExperiments/mpu_server.py & > /home/orangepi/log.txt 2>&1

@app.route('/')
def hello_world():
    return "%.2f°C" % get_temperature()

app.run(host='0.0.0.0')