#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import call
import random
import datetime
import urllib2
import json

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate(busnum = 1)
lcd.begin(16,2)
lcd.clear()
        
def bounce(lcdScreen):
    screen = lcdScreen
    for row in xrange(2):
        for column in xrange(16):
                screen.setCursor(column, row)
                screen.message("#")
                sleep(1)
                screen.clear()
            
def time(lcdScreen):
    screen = lcdScreen
    screen.clear()
    format = "%a %b %d\n%H:%M:%S %Y"
    today = datetime.datetime.today()
    s = today.strftime(format)
    screen.message(s)

def weather(lcdScreen):
    screen = lcdScreen
    screen.clear()
    f = urllib2.urlopen('http://api.wunderground.com/api/69e962e1a8ee7b82/geolookup/conditions/q/MI/Detroit.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    loc_city = parsed_json['location']['city']
    loc_state = parsed_json['location']['state']
    temp_f = parsed_json['current_observation']['temp_f']
    message = '{city}, {state}\n{temp} F'.format(city=loc_city, state=loc_state, temp=temp_f)
    screen.message(message)
    f.close()
    

btn = ((lcd.LEFT),
       (lcd.UP),
       (lcd.DOWN),
       (lcd.RIGHT),
       (lcd.SELECT))

prev = -1
flag = 0
while True:
    for b in btn:
        if lcd.buttonPressed(b):
            if b is not prev:
                if b is lcd.DOWN:
                    time(lcd)
                    flag = 0
                    prev = b
                if b is lcd.LEFT:
                    weather(lcd)
                    prev = b
                    flag = 1
            break
        else:
            if flag is 0:
                time(lcd)
                sleep(1)
