#!/usr/bin/python3

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

heartbeat_gap = 0.07 # gap between beats

def heart_beat(strip, elevation, distance, direction):
  # print(elevation)
  # print(distance)
  # print(direction)
  pix = patterns.get('pin_out')[elevation-1][direction/45]
  # print(pix)
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

# person approaching
# person begins at 0 degrees 25 feet away
# walks towards you and moves to the left, 10 feet away
# continues past to 25 feet
def person_approaches(strip, ele):
  distances = [3, 2, 1, 0, 1, 2, 3]
  directions = [0, 0, 45, 90, 135, 180, 180]
  
  motion = [[(i, j) for i in distances] for j in directions]
  pix = motion[i][j]

  for x in range(len(distances)): 
    strip.setPixelColor(pix,pulse_on)
    strip.show()
    print(pix)
    time.sleep(heartbeat_gap)

    strip.setPixelColor(pix,pulse_off)
    strip.show()
    print(pix)
    time.sleep(heartbeat_gap)

    strip.setPixelColor(pix,pulse_on)
    strip.show()
    print(pix)
    time.sleep(heartbeat_gap)

    strip.setPixelColor(pix,pulse_off)
    strip.show()
    print(pix)
    time.sleep(beat)


if __name__ == '__main__':
  # Create NeoPixel object with appropriate configuration.
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  # Initialize the library (must be called once before other functions).
  strip.begin()
  print ('Press Ctrl-C to quit.')
  try:
    while(True):
      person_approaches(strip, 1)

  except KeyboardInterrupt:
    colorWipe(strip, Color(0,0,0), 10)
    print("Goodbye World")
