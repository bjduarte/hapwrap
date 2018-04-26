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



def colorWipe(strip, color, wait_ms=50):
<<<<<<< HEAD
=======

>>>>>>> 1e9248040c5f2cec1232c1a81c03978cf551ecd0
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


# Main program logic follows:
if __name__ == '__main__':
<<<<<<< HEAD
=======
    # Process arguments
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    #parser.add_argument('elevation')
    #parser.add_argument('distance')
    #parser.add_argument('direction')
    #args = parser.parse_args()

    #demo_input [elevation (0-2),distance (10-25),direction (0-5)
    demo_input = [[0,20,3],[1,10,5],[2,25,0]]

>>>>>>> 1e9248040c5f2cec1232c1a81c03978cf551ecd0
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    colorWipe(strip, Color(255, 255, 255),100) # Red wipe

<<<<<<< HEAD
=======
    print ('Press Ctrl-C to quit.')
    #if not args.clear:
    #    print('Use "-c" argument to clear LEDs on exit')

    try:

    #    while True:
    #   print('Eyes On Demo')
    #     print('\nEnter elevation, distance, direction:')
    #    print ("Elevation: " + elevation)
    #      print ("Distance: " + distance)
    #      print ("direction: " + direction)
    #      
            # print ('Color wipe animations.')
        colorWipe(strip, Color(255, 255, 255),2000)  # Red wipe
            # colorWipe(strip, Color(0, 255, 0))  # Blue wipe
            # colorWipe(strip, Color(0, 0, 255))  # Green wipe
            # print ('Theater chase animations.')
            # theaterChase(strip, Color(127, 127, 127))  # White theater chase
            # theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            # theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
            # print ('Rainbow animations.')
            # rainbow(strip)
            # rainbowCycle(strip)
            # theaterChaseRainbow(strip)
>>>>>>> 1e9248040c5f2cec1232c1a81c03978cf551ecd0

    except KeyboardInterrupt:
       # if args.clear:
       colorWipe(strip, Color(0,0,0), 10)
