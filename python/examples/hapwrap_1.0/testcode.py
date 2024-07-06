# hapwrap/bin/python3

import json
import adafruit_blinka.board.raspberrypi.raspi_4b
import board
import neopixel
import sys
import time

#LED strip configuration:
STRINGS = [0, 1, 2, 3]
HAXYLS_PER_STRING = 3
STRING1 = board.D10
STRING2 = board.D12
STRING3 = board.D18
STRING4 = board.D21
ORDER = neopixel.RGB
#haxylPin = 10 # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10 # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip1 = neopixel.NeoPixel(STRING1, HAXYLS_PER_STRING, auto_write=True, pixel_order=ORDER)
strip2 = neopixel.NeoPixel(STRING2, HAXYLS_PER_STRING, auto_write=True, pixel_order=ORDER)
strip3 = neopixel.NeoPixel(STRING3, HAXYLS_PER_STRING, auto_write=True, pixel_order=ORDER)
strip4 = neopixel.NeoPixel(STRING4, HAXYLS_PER_STRING, auto_write=True, pixel_order=ORDER)

# parameter order (Red, Green, Blue)
pulseOn = (168, 0, 168)
pulseStop = (168, 168, 0)
pulseOff = (0, 0, 0)
reverseCurrent = 0.4

# Times of heartbeat
heartbeatPulse = 3
# gap between beats
heartbeatGap = 0.06 
# duration beat is on
heartbeat_pulse = 0.55 

expressions  ={
    'happy' : [0, 1, 2, 3],
    'angry' : [4, 5, 6, 7],
    'neutral' : [8, 9, 10, 11],
    'haxylIndex' : [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19,]]
}

with open('expressions.json', 'w') as json_file:
    json.dump(expressions, json_file)


def patternBuilder():
  beat = 0
  pattern = {}

  with open('expressions.json') as json_file:
    data = json.load(json_file)
        

  userimput = int(input("Enter 1 for Happy, 2 for Angry, 3 for Neutral"))
  if (userimput == 1):
    pattern = data.get('happy', [])
    print ("Expression is Happy",+pattern[0])
    beat = 0.25
  elif (userimput == 2):
    pattern = data.get('angry', [])
    print ("Expression is Angry",+ pattern[0])
    beat = 0.50
  elif (userimput == 3):
    pattern = data.get('neutral', [])
      # print(frame)
    print ("Expression is Neutral",+ pattern[0])
    beat = 1.00


#   print("Beginning Heartbeat")
  for x in range(heartbeatPulse):

# Turn on the Haxyls 
    strip1 = (pattern[0], pulseOn)
    print("Haxyls on strip 1 are on" + str(strip1))
    strip2 = (pattern[1], pulseOn)
    print('Haxyls on strip 2 are on' + str(strip2))
    strip3 = (pattern[2], pulseOn)
    print('Haxyls on strip 3 are on' + str(strip3))
    strip4 = (pattern[3], pulseOn)
    print('Haxyls on strip 4 are on' + str(strip4))
    time.sleep(beat)

      # Turn off Haxyls by reversing current
    print('Reverse Current')
    strip1 = (pattern[0], pulseStop)
    print("Haxyls on strip 1 are being reversed" + str(strip1))
    strip2 = (pattern[1], pulseStop)
    print("Haxyls on strip 2 are being reversed" + str(strip1))
    strip3 = (pattern[2], pulseStop)
    print("Haxyls on strip 3 are being reversed" + str(strip1))
    strip4 = (pattern[3], pulseStop)
    print("Haxyls on strip 4 are being reversed" + str(strip1))
    time.sleep(reverseCurrent)

      # Power off Haxyls for heartbeat duration
    print("Haxyls are off")
    strip1 = (pattern[0], pulseOff)
    print("Haxyls on strip 1 are off" + str(strip1))
    strip2 = (pattern[1], pulseOff)
    print("Haxyls on strip 2 are off" + str(strip1))
    strip3 = (pattern[2], pulseOff)
    print("Haxyls on strip 3 are off" + str(strip1))
    strip4 = (pattern[3], pulseOff)
    print("Haxyls on strip 4 are off" + str(strip1))
    time.sleep(heartbeatGap)

# beginning second heartbeat pulse 
    strip1 = (pattern[0], pulseOn)
    print("Haxyls on strip 1 are on" + str(strip1))
    strip2 = (pattern[1], pulseOn)
    print('Haxyls on strip 2 are on' + str(strip2))
    strip3 = (pattern[2], pulseOn)
    print('Haxyls on strip 3 are on' + str(strip3))
    strip4 = (pattern[3], pulseOn)
    print('Haxyls on strip 4 are on' + str(strip4))
    time.sleep(beat)

      # Turn off Haxyls by reversing current
    print('Reverse Current')
    strip1 = (pattern[0], pulseStop)
    print("Haxyls on strip 1 are being reversed" + str(strip1))
    strip2 = (pattern[1], pulseStop)
    print("Haxyls on strip 2 are being reversed" + str(strip1))
    strip3 = (pattern[2], pulseStop)
    print("Haxyls on strip 3 are being reversed" + str(strip1))
    strip4 = (pattern[3], pulseStop)
    print("Haxyls on strip 4 are being reversed" + str(strip1))
    time.sleep(reverseCurrent)

      # Power off Haxyls for heartbeat duration
    print("Haxyls are off")
    strip1 = (pattern[0], pulseOff)
    print("Haxyls on strip 1 are off" + str(strip1))
    strip2 = (pattern[1], pulseOff)
    print("Haxyls on strip 2 are off" + str(strip1))
    strip3 = (pattern[2], pulseOff)
    print("Haxyls on strip 3 are off" + str(strip1))
    strip4 = (pattern[3], pulseOff)
    print("Haxyls on strip 4 are off" + str(strip1))
    time.sleep(heartbeatGap)




def main():
  print("Beginning Main")
  patternBuilder()




if __name__ == '__main__':
  main()
