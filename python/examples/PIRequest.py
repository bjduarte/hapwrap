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

# lists of all the possible components that make up a pattern
elevation = [0, 1, 2]
distance = [0, 1, 2]
direction = [0, 1, 2, 3, 4, 5, 6, 7]

#dictionary containning all static patterns
patternDict = {}
#iterate through each component to create a list of patterns
#elevation, distance, direction
pat = dynamicPattern.pattern_builder()

# create list of keys, necessary for calling dynamic patterns
for i in pat:
    dKeyList.append(i)

num = 0
patternList = []
for i in elevation:
  for j in distance:
    for k in direction:
      pattern = [num, i, j, k]
      patternList.append(pattern)
      #patternDict['pattern list'] = patternList
      num += 1

# Patterns dictionary containing object positions
patterns = {
    'elevation' : [1, 2, 3],
    'distance' : [10, 15, 20], 
    'direction' : [[0, 45, 90, 135, 180, 225, 270, 315],[315, 270, 225, 180, 135, 90, 45, 0],[0, 45, 90, 135, 180, 225, 270, 315]],
    'pin_out' : [[0,1,2,3,4,5,6,7],[15, 14, 13, 12, 11, 10, 9, 8],[16,17,18,19,20,21,22,23]] }



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
    for currentBeat in j:
        # print pat.get(currentDynamicPattern)
        print currentBeat
        elevation = currentBeat[0]
        distance = currentBeat[1]
        direction = currentBeat[2]
        print ('elevation: ' + str(elevation) + ' ' + 'distance: ' + str(distance) + ' ' + 'direction: ' + str(direction))
        print (currentDynamicPattern)
        pix = patterns.get('pin_out')[elevation][direction]
        print("pix = " + str(pix))
        beat = 0

        if (distance == 0):
            # print ("distance is 0")
            beat = 0.25
        elif (distance == 1):
            # print ("distance is 1")
            beat = 0.50
        elif (distance == 2):
            # print ("distance is 2")
            beat = 1.00

        #PixPointer Pattern
            pixPointer = patterns.get('pin_out')[1][direction]
            print("pixPointer = " + str(pixPointer))
            strip.setPixelColor(pixPointer,pulse_on)
            print ("On")
            strip.show()
            print(beat)
            time.sleep(0.99)

            strip.setPixelColor(pixPointer,pulse_off)
            print ("Off")
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)
            print("Beginning Heartbeat")

        # Heartbeat pattern for 10 through 20 feet
        if ((distance == 2) or (distance == 1) or (distance == 0)):
            for x in range(heartbeat_pulse):
                strip.setPixelColor(pix,pulse_on)
                print ("On")
                strip.show()
                print(beat)
                time.sleep(heart_gap)

                strip.setPixelColor(pix,pulse_off)
                print ("Off")
                strip.show()
                print(beat)
                time.sleep(heartbeat_gap)

                strip.setPixelColor(pix,pulse_on)
                print ("On")
                strip.show()
                print(beat)
                time.sleep(heart_gap)

                strip.setPixelColor(pix,pulse_off)
                print ("Off")
                strip.show()
                print(beat)
                time.sleep(beat)
    return 'JSON posted'

app.run(host='0.0.0.0', port=   8080)


  
