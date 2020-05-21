# Orange Pi One Experiments

Contains a few sketches and pinout schematics for the Orange Pi One.
Also has an identification sheet for sensors, since they are often not labeled.

The sketches should be self-explanatory.

## Getting Started

### Insalling the IO library

`sudo pip3 install OrangePi.GPIO`
 
 ## Troubleshooting:
 Typical things that can go wrong:
 - Not all color LEDs survive 3.3V
 - Not all RGB LED modules have resistors built in
 - Double check your poles, the short leg of the LED has to be connected to GND
 - Just because a pin can be setup as GPIO IN/OUT, doesn't mean they work properly as such. Best stick to the PA/PD/PC pins (see schematics)