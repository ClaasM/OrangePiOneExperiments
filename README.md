# Orange Pi One Experiments

Contains a few sketches and pinout schematics for the Orange Pi One.
Also has an identification sheet for sensors, since they are often not labeled.

The sketches should be self-explanatory.

## Getting Started

### Installing Python Header files

Required to install IO libraries, such as OrangePi.GPIO

`sudo apt-get install python3-dev`

### Installing the IO library

`sudo pip3 install OrangePi.GPIO`

### Configuring I2C

Only required to use the MPU.
 
`sudo apt-get install python3-smbus i2c-tools`

`armbian-config` -> `system` -> `hardware` -> `i2c0` and use space key to select. Save and reboot.

 ## Troubleshooting:
 Typical things that can go wrong:
 - Not all color LEDs survive 3.3V
 - Not all RGB LED modules have resistors built in
 - Double check your poles, the short leg of the LED has to be connected to GND
 - Just because a pin can be setup as GPIO IN/OUT, doesn't mean they work properly as such. Best stick to the PA/PD/PC pins (see schematics)