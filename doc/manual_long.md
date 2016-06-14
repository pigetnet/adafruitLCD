| /do/adafruitLCD/checkI2C   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |
| 1. I2C is not enable       |                        |

| /do/adafruitLCD/checkRGB   |                                                                 |
|:---------------------------|:----------------------------------------------------------------|
| Info                       | [alpha] [undocumented]                                          |
| Modules                    | cd /do/adafruitLCD/pythonLib/examples;python char_lcd_plate.py, |

| /do/adafruitLCD/install                         |                                                                                                                                                                                                                                                                                                                     |
|:------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                                            | [alpha] [undocumented]                                                                                                                                                                                                                                                                                              |
| Softwares                                       | python-smbus, i2c-tools, build-essential, python-dev, python-smbus, python-pip, git, python-rpi.gpio,                                                                                                                                                                                                               |
| Modules                                         | if [ -d /do/adafruitLCD/pythonLib ];then, rm -rf /do/adafruitLCD/pythonLib, /system/gitcloner adafruit/Adafruit_Python_CharLCD /do/adafruitLCD/pythonLib, if [ -d /do/adafruitLCD/pythonLib ];then, cd /do/adafruitLCD/pythonLib;python setup.py install > /tmp/adafruit_lcd.log 2>&1,                              |
| System                                          | /system/install python-smbus, /system/install i2c-tools, /system/install build-essential, /system/install python-dev, /system/install python-smbus, /system/install python-pip, /system/install git, /system/install python-rpi.gpio, /system/gitcloner adafruit/Adafruit_Python_CharLCD /do/adafruitLCD/pythonLib, |
| 1. Adafruit LCD Shield module                   |                                                                                                                                                                                                                                                                                                                     |
| 1. Check dependencies                           |                                                                                                                                                                                                                                                                                                                     |
| 10. Download library                            |                                                                                                                                                                                                                                                                                                                     |
| 11. Install library                             |                                                                                                                                                                                                                                                                                                                     |
| 12. Enable I2C                                  |                                                                                                                                                                                                                                                                                                                     |
| 13. You need to reboot to enable the LCD screen |                                                                                                                                                                                                                                                                                                                     |
| 14. I cant download Adafruit LCD library        |                                                                                                                                                                                                                                                                                                                     |

| /do/adafruitLCD/write   |                                                        |
|:------------------------|:-------------------------------------------------------|
| Info                    | [alpha] [undocumented]                                 |
| Modules                 | python /do/adafruitLCD/python/write.py 1.0 1.0 1.0 $1, |

