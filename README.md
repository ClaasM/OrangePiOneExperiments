# Orange Pi One Experiments

Contains a few sketches and pinout schematics for the Orange Pi One.
Also has an identification sheet for sensors, since they are often not labeled.

The sketches should be self-explanatory.

## Getting Started

### Creating a bootable SD card (Armbian Focal)

Focal means based on Ubuntu.
Used for most of these scripts, generally works better out of the box.

Default username: `root`

Default password: `1234` 

You are then prompted to set a secure password.

### Creating a bootable SD card (Ubuntu)

(Using Ubuntu image from OrangePi)

Default username: `orangepi`

Default password: `orangepi`

### Connect to Wifi

After connecting via Ethernet, check router interface for the Pi's IP.

SSH into it: `ssh <username>@<ip>`
 
Use `nmtui` to connect to WiFi.

Again, get the WiFi IP from e.g. your Router's interface.
Validate you can SSH via that IP as well.
You can now disconnect the Ethernet connection.
 
Alternatively, you can edit the image - most OS's can be configured to connect to a WiFi on initial boot.

### Installing Python Header files

Required to install IO libraries, such as OrangePi.GPIO

`sudo apt-get install python3-dev`

### Installing the IO library

`sudo pip3 install OrangePi.GPIO`

### Configuring I2C

Only required to use the MPU.
 
`sudo apt-get install python3-smbus i2c-tools`

`armbian-config` -> `system` -> `hardware` -> `i2c0` and use space key to select. Save and reboot.

### Configurint W1 (one wire)

https://blog.ja-ke.tech/2019/01/21/DS18B20-armbian.html

 ## Troubleshooting:
 
 Typical things that can go wrong (hardware):
 - Not all color LEDs survive 3.3V
 - Not all RGB LED modules have resistors built in
 - Double check your poles, the short leg of the LED has to be connected to GND
 - Just because a pin can be setup as GPIO IN/OUT, doesn't mean they work properly as such. Best stick to the PA/PD/PC pins (see schematics)
 - PIN 1 3.3V didn't work on my board, had to use the other 3.3V pin
 - Relay didn't switch on 3.3V, needed 5V
 
 ### Troubleshooting IO pins
 
E.g. for PA12 (called PS12 in schematic for some reason)

``` 
cd /sys/class/gpio
echo 12 > export
echo out > gpio12/direction
echo 1 > gpio12/value
cat gpio12/value
echo 0 > gpio12/value
echo 12 > unexport
```