#!/usr/bin/python3

import time
import json
import sys
import random
from neopixel import *
from dynamic_pattern_list_builder import *


# LED strip configuration:
LED_COUNT = 24 # Number of LED pixels.
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
heartbeat_gap = 0.07 # gap between beats

# Dictionary containing object positions
patterns = {
  'elevation' : [1, 2, 3],
  'distance' : [10, 15, 20, 25], 
  'direction' : [[0, 45, 90, 135, 180, 225, 270, 315],[315, 270, 225, 180, 135, 90, 45, 0],[0, 45, 90, 135, 180, 225, 270, 315]],
  'pin_out' : [[0,1,2,3,4,5,6,7],[8,9,10,11,12,13,14,15],[16,17,18,19,20,21,22,23]]
}

# global list declarations and class initialization
dynamicPattern = Dynamic_pattern_list_builder() # class initialization
pat = dynamicPattern.pattern_builder() # dynamic_pattern declaration
randNumList = [] # list of random numbers
visitedPattern = [] # list of visited patterns
dList = [] # list of keys

# create list of dictionary keys
for i in pat:
  dList.append(i)


# json handler to read in dictionary of dynamic patterns
#f = open('dynamic_pattern_list.json', 'r')
#fin = json.load(f)
#f.close()

#for i in fin:
#    print(fin['dynamic patterns'])

# creates the heartbeat pulse
# handles 10, 15, 20  feet heartbeat patterns
# if 25 feet, creates sonar pulse
def heart_beat(strip, elevation, distance, direction):
  pix = patterns.get('pin_out')[elevation-1][direction/45]

  beat = 0

  if (distance == 10):
    beat = 0.300
  elif (distance == 15):
    beat = 0.650
  elif (distance == 20):
    beat = 1.000
  elif (distance == 25):
    beat = 1.00
    heart_gap = 0.5

# sonar pulse for 25 feet
    for i in range(heartbeat_pulse):
      strip.setPixelColor(pix,pulse_on)
      strip.show()
      time.sleep(heart_gap)

      strip.setPixelColor(pix,pulse_off)
      strip.show()
      time.sleep(beat)

# Heartbeat pattern for 10 through 20 feet
  for x in range(heartbeat_pulse): 
    strip.setPixelColor(pix,pulse_on)
    strip.show()
    time.sleep(heartbeat_gap)

    strip.setPixelColor(pix,pulse_off)
    strip.show()
    time.sleep(heartbeat_gap)

    strip.setPixelColor(pix,pulse_on)
    strip.show()
    time.sleep(heartbeat_gap)

    strip.setPixelColor(pix,pulse_off)
    strip.show()
    time.sleep(beat)

# handler for dynamic patterns
# calls dynamic_pattern_list_builder.py
# randomly selects a dynamic pattern and calls all the beats to simulate that pattern
def dynamic_pattern_handler(strip):
  while (len(randNumList) < 23):
    rNum = random.randint(0, 22)
    while (rNum not in randNumList):
      randNumList.append(rNum)
      dBeat = dList[rNum]
      visitedPattern.append(dBeat)


  for dPat in visitedPattern:
    print(dPat)
    for beat in pat.get(dPat):
      elevation = beat[0]
      distance = beat[1]
      direction = beat[2]
      print ('elevation: ' + str(elevation) + ' ' + 'distance: ' + str(distance) + ' ' + 'direction: ' + str(direction))
    heart_beat(strip, elevation, distance, direction)


if __name__ == '__main__':

  # Create NeoPixel object with appropriate configuration.
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  # Initialize the library (must be called once before other functions).
  strip.begin()
  print ('Press Ctrl-C to quit.')
  try:
    dynamic_pattern_handler(strip)

  except KeyboardInterrupt:
    colorWipe(strip, Color(0,0,0), 10)
    print("Goodbye World")
