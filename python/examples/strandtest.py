#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse
import sys

# LED strip configuration:
LED_COUNT      = 18      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


pulse_on = Color(255, 255, 255)
pulse_off = Color(0, 0, 0)
elevationL= [[0,1,2,3,4,5],[11,10,9,8,7,6],[12,13,14,15,16,17]]
num_hearteats = 3
hearttime = 0.05

def buzz(strip, elevation, distance, direction):
    # elevation = 1,2,3
    # distance 10, 15, 20 ,25  # .35, .7, 1.05, 1.4
    # direction -0,1,2,3,4,5

    distSlep = ((distance/5) * .35) 
    pix = elevationL[elevation-1][direction]

    for _ in xrange(num_hearteats): 

        strip.setPixelColor(pix,pulse_on)#on 
        strip.show()
        time.sleep(hearttime)

        strip.setPixelColor(pix,pulse_off)#off
        strip.show()
        time.sleep(hearttime)

        strip.setPixelColor(pix,pulse_on)#on
        strip.show()
        time.sleep(hearttime)

        strip.setPixelColor(pix,pulse_off)#delay
        strip.show()
        time.sleep(distSlep)



#Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


# Main program logic follows:
if __name__ == '__main__':

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    print ('Press Ctrl-C to quit.')
    try:

        while True:
          inp = raw_input("\ninput elvation, distance and direction seperated by spaces!\n")
          inpList = inp.split(" ")
          buzz(strip,int(inpList[0]), int(inpList[1]), int(inpList[2]))


    except KeyboardInterrupt:
        colorWipe(strip, Color(0,0,0), 10)
