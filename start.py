#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import call
import glob
import random
# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate(busnum = 1)
lcd.begin(16,2)
lcd.clear()

messages = (("working"), ("working\nsucks"), ("weed weed"),("yea..."),("why why"))

music_directory = "/root/music/*.mp3"

songs = glob.glob(music_directory)
#list songs in directory
def list_songs(directory):
    if directory:
        mp3s = glob.glob(directory)
    else:
        mp3s = glob.glob("/root/music/*.mp3")

    for mp3 in mp3s:
        print mp3
        lcd.clear()
        lcd.message(mp3)
        sleep(5)
    
def random_message(lcdScreen):
    screen = lcdScreen
    screen.clear()
    for index in range(0,4):
        screen.message(messages[index])
    
def timed_messages(lcdScreen, iterations):
    screen = lcdScreen
    screen.clear()
    count = 0
    while count < iterations:
        index = random.randrange(0,4)
        screen.message(messages[index])
        sleep(5)
        screen.clear()
        screen.message(count)
        sleep(1)
        screen.clear()
        count = count + 1


# Poll buttons, display message & set backlight accordingly
btn = ((lcd.LEFT),
       (lcd.UP),
       (lcd.DOWN),
       (lcd.RIGHT),
       (lcd.SELECT))

prev = -1

while True:
    for b in btn:
        if lcd.buttonPressed(b):
            if b is not prev:
                if b is lcd.SELECT:
                    random_messages(lcd)              
                prev = b
                if b is lcd.UP:
                    while True:
                        timed_messages(lcd, 500)            
            break
