# boot.py -- run on boot-up
from machine import Pin, SoftI2C
from stepper import Stepper
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
i2c = SoftI2C(scl=Pin(22), sda=Pin(17), freq=10000) #I2C for ESP32
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
luzverde = Pin(26, Pin.OUT)

luzverde.value(1)
lcd.putstr("Inicializando...")
time.sleep(3)
lcd.clear()