#!/usr/bin/python
import sys
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
lcd.clear()
lcd.message(sys.argv[4])

