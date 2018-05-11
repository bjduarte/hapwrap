#!/usr/bin/python

import time
import json
import sys
from neopixel import *


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
heart_beat_pulse = 3
heart__beat_gap = 0.05

# Dictionary containing object positions
patterns = {
  'elevation' : [1, 2, 3],
  'distance' : [10, 15, 20, 25], 
  'direction' : [[0,1,2,3,4,5, 6, 7],[15, 14, 13, 12, 11, 10, 9, 8],[16, 17, 18, 19, 20, 21, 22, 23]]
}


def heart_beat(elevation, distance, direction):
  pix = [elevation][direction]

    for _ in xrange(heart_beat_pulse): 

        strip.setPixelColor(pix,pulse_on)
        print ("beat1")
        strip.show()
        time.sleep(heart_beat_gap)

        strip.setPixelColor(pix,pulse_off)
        print ('gap')
        strip.show()
        time.sleep(heart_beat_gap)

        strip.setPixelColor(pix,pulse_on)
        print ('beat2')
        strip.show()
        time.sleep(heart_beat_gap)

        strip.setPixelColor(pix,pulse_off)
        print ('gap')
        strip.show()
        time.sleep(0.35)
        print ('heart beat1')


def get_pattern(strip, ele, dist, dir):
  elevation = patterns.get('elevation')[ele]
  distance = patterns.get('distance')[dist]

  if (elevation == 1):
    direction = patterns.get('direction')[dir]
  elif (elevation == 2):
    direction = (patterns.get('direction')[dir] + 8)
  else:
    direction = (patterns.get('direction')[dir] + 8)

  #print (elevation, distance, direction)
  heart_beat(elevation, distance, direction)

  return (elevation, distance, direction)


if __name__ == '__main__':
  # Create NeoPixel object with appropriate configuration.
  trip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  # Initialize the library (must be called once before other functions).
  strip.begin()
  print ('Press Ctrl-C to quit.')

  try:
    while True:
      objectInput = input("\nEnter the elvation, distance, and direction!\n")
      objectPosition = objectInput.split(" ")
      pat = get_pattern(int(objectPosition[0]), int(objectPosition[1]), int(objectPosition[2]))
      print('input: ', pat)

  except KeyboardInterrupt:
    colorWipe(strip, Color(0,0,0), 10)
    print("Goodbye World")
