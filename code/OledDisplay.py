from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.text("Welcome To", 0, 0)
oled.text("Interfacing RPI PICO", 5, 20)
oled.text("with OLED", 22, 30)
oled.show()
oled.pixel(10,10,1)
oled.show()