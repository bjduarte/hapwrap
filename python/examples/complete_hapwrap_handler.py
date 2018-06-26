#!/usr/bin/python3

import sys
import json
import io
import random
from dynamic_pattern_list_builder import *

class JSON_update:
  # lists of all the possible components that make up a pattern
  # elevation = ['chair', 'vehicle', 'person']
  # distance = [10, 15, 20, 25]
  # direction = [0, 45, 90, 135, 180, 225, 270, 315]
  elevation = [0, 1, 2]
  distance = [0, 1, 2, 3]
  direction = [0, 1, 2, 3, 4, 5, 6, 7]
  
  # global list declarations for static patterns
  sRandNumList = [] # list of random numbers for static patterns
  visitedStaticPattern = [] # list of visited static patterns
  patternList = [] # list of lists containing static patterns
  patternDict = {} # global dictionary containing all data

  # global list declarations and class initialization for dynamic patterns
  dynamicPattern = Dynamic_pattern_list_builder() # initializes class to get dynamic patterns
  pat = dynamicPattern.pattern_builder() # dynamic_pattern is method to get dynamic pattern lists
  dRandNumList = [] # list of random numbers for dynamic patterns
  visitedDynamicPattern = [] # list of visited dynamic patterns
  dKeyList = [] # list of keys

# create list of keys, necessary for calling dynamic patterns
for i in pat:
  dKeyList.append(i)

  # iterate through each component to create a list of patterns
  # elevation, distance, direction
  def create_patterns(self):
    num = 0
    for i in self.elevation:
      for j in self.distance:
        for k in self.direction:
          pattern = [i, j, k]
          self.patternList.append(pattern)
          self.patternDict['pattern list'] = self.patternList
          num += 1

# STATIC Pattern Selector
  # generates a random number and calls a pattern
  # bind with "next button" event handler from GUI
  def static_handler(self):
    currentPattern = []

    while (len(self.sRandNumList) < 48):
      rNum = random.randint(0, 47)
      while (rNum not in self.sRandNumList):
        self.sRandNumList.append(rNum)
        currentPattern = self.patternList[rNum]
        self.visitedStaticPattern.append(currentPattern)
        self.patternDict['visited dynamic patterns'] = self.visitedStaticPattern
        # print(currentPattern)

    return currentPattern


  # DYNAMIC Pattern handler
  # calls dynamic_pattern_list_builder.py
  # randomly selects a dynamic pattern and calls all the beats to simulate that pattern
  # bind with "Next Dynamic button" event handler from GUI
  def dynamic_handler(self):
    while (len(self.dRandNumList) < 23):
      rNum = random.randint(0, 22)
      while (rNum not in self.dRandNumList):
        self.dRandNumList.append(rNum)
        currentPattern = self.dList[rNum]
        self.visitedDynamicPattern.append(currentPattern)
        self.patternDict['visited dynamic patterns'] = self.visitedDynamicPattern

    # for dPat in self.visitedDynamicPattern:
    #   print(dPat)
    #   for currentBeat in self.pat.get(dPat):
    #     elevation = currentBeat[0]
    #     distance = currentBeat[1]
    #     direction = currentBeat[2]
        # print ('elevation: ' + str(elevation) + ' ' + 'distance: ' + str(distance) + ' ' + 'direction: ' + str(direction))

    return currentPattern


  # keep track of participants answers
  # radio button presses will be read in and saved 
  def user_response(self):
    incorrect_response = [ele, dist, dir] # comes from radiobuttons
    user_response = []
    user_response.append(incorrect_response)
    patternDict['user response'] = user_response

  # write to JSON
  # visited dynamic patterns, visited static patterns, current pattern, user response
  def write_data(self):
    json = json.dumps(self.patternDict)
    f = open("userData.json","w")
    f.write(json)
    f.close()

  # read in visited patterns
  def read_data(self):
    f = open('userData.json', 'r')
    fin = json.load(f)
    f.close()

    for i in fin:
        print(fin['visited static patterns'], fin['user response'], fin['visited dynamic patterns'], fin['user response'])

if __name__ == '__main__':
  dPattern = JSON_update()
  print ("Press CTRL c to quit")
  
  try:
    dPattern.create_patterns()
    test = dPattern.static_handler()
    print (test)
    
    test2 = dPattern.dynamic_handler()
    print(test2)

  except KeyboardInterrupt:
    print 'Interrupted'
    try:
      sys.exit(0)
    except SystemExit:
      sys.exit(0)
