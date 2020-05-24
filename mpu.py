# Connected to the default SCL/SDA pins of the board.

import smbus

bus = smbus.SMBus(0)
address = 0x68


def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg + 1)
    value = (h << 8) + l
    return value


def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val


def get_temperature():
    temp = read_word_2c(0x41)
    temp_c = temp / 340.00 + 36.53
    return temp_c


# Just getting temperature, but accelerometer/gyro are read similarly.
print("Temperature")
print("--------")
print("%.2f°C" % get_temperature())
