# Soil Moisture

Using Orange Pi One.

## Materials

- OPi One
- Capactive Soil Moisture Sensor v1.2
- ADS1115


## Wiring

- See wiring.png (SDA0/SCK0 are also pins 3 and 5 on orangepi)

## Setup

sudo armbian-config

OR

sudo nano /boot/armbianEnv.txt
overlays=i2c0

(Also need W1)

##

Running in background:


## Troubleshooting

- All sensors give the same reading: Use a lower sample rate
    
    