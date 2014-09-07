#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

# Poll buttons, display message & set backlight accordingly
btn = ((lcd.LEFT  , 'Fuck Techno.'              , lcd.ON),
       (lcd.UP    , 'Fuck Detroit.'     , lcd.ON),
       (lcd.DOWN  , 'Fuck yea!'    , lcd.ON),
       (lcd.RIGHT , 'Fuck Fuck\nFuck Fuck', lcd.ON),
       (lcd.SELECT, ''                          , lcd.ON))
prev = -1
while True:
    for b in btn:
        print b
        if lcd.buttonPressed(b[0]):
            if b is not prev:
                lcd.clear()
                lcd.message(b[1])
                lcd.backlight(b[2])
                prev = b
            break
