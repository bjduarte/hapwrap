#!usr/bin/python3

from flask import Flask
from flask import request
import json
from neopixel import *
import sys
import json
import random
import shutil
import time

#LED strip configuration:
LED_COUNT = 24 # Number of LED Labels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN = 10 # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10 # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

pulse_on = Color(255, 255, 255)
pulse_off = Color(0, 0, 0)

heartbeat_pulse = 3
heartbeat_gap = 0.06 # gap between beats
heart_gap = 0.55 # duration beat is on

# Patterns dictionary containing dynamic positions
patterns = {
    'elevation' : [1, 2, 3],
    'distance' : [10, 15, 20], 
    'direction' : [[0, 45, 90, 135, 180, 225, 270, 315],[315, 270, 225, 180, 135, 90, 45, 0],[0, 45, 90, 135, 180, 225, 270, 315]],
    'pin_out' : [[23, 22, 21, 20, 19, 18, 17, 16],[15, 14, 13, 12, 11, 10, 9, 8],[7, 6, 5, 4, 3, 2, 1, 0]] }

# json flask request
app = Flask(__name__)

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    print(request.get_data())
    j = json.loads(request.get_data())
    content = request.get_json()
    print (j)
#    print('Output ' + j['first_name'])
    for currentPattern in j:
        print (currentPattern)
        elevation = currentPattern[0]
        distance = currentPattern[1]
        direction = currentPattern[2]
        print ('elevation: ' + str(elevation) + ' ' + 'distance: ' + str(distance) + ' ' + 'direction: ' + str(direction))

        pix = patterns.get('pin_out')[elevation][direction]
        print("pix = " + str(pix))
        beat = 0

        if (distance == 0):
            print ("distance is 10")
            beat = 0.25
        elif (distance == 1):
            print ("distance is 15")
            beat = 0.50
        elif (distance == 2):
            print ("distance is 20")
            beat = 1.00

        #PixPointer Pattern
            pixPointer = patterns.get('pin_out')[1][direction]
            print("pixPointer = " + str(pixPointer))
            strip.setPixelColor(pixPointer,pulse_on)
            print ("Pointer Beat On")
            strip.show()
            time.sleep(0.99)

            strip.setPixelColor(pixPointer,pulse_off)
            print ("Pointer Beat Off")
            strip.show()
            print("beat", beat)
            time.sleep(heartbeat_gap)
            print("Beginning Heartbeat")

        # Heartbeat pattern for 10 through 20 feet
        if ((distance == 2) or (distance == 1) or (distance == 0)):
            for x in range(heartbeat_pulse):
                strip.setPixelColor(pix,pulse_on)
                print ("On")
                strip.show()
                print("beat", beat)
                time.sleep(heart_gap)

                strip.setPixelColor(pix,pulse_off)
                print ("Off")
                strip.show()
                time.sleep(heartbeat_gap)

                strip.setPixelColor(pix,pulse_on)
                print ("On")
                strip.show()
                print("beat", beat)
                time.sleep(heart_gap)

                strip.setPixelColor(pix,pulse_off)
                print ("Off")
                strip.show()
                time.sleep(beat)
    return 'JSON posted'

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()
app.run(host='0.0.0.0', port=   8080)


  
