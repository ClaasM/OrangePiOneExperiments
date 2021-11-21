# Soil Moisture

Using Orange Pi One.

## Materials

- OPi One
- Capactive Soil Moisture Sensor v1.2
- ADS1115


## Wiring

- See wiring.png

## Setup

sudo armbian-config

OR

sudo nano /boot/armbianEnv.txt
overlays=i2c0

## Troubleshooting

- All sensors give the same reading: Use a lower sample rate
    
    