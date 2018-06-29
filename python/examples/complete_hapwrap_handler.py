#!/usr/bin/python3

import sys
import json
import io
import random
from dynamic_pattern_list_builder import *

class Complete_hapwrap_handler:
  

  def __init__(self):
    self.dynamicPattern = Dynamic_pattern_list_builder() # initializes class to get dynamic patterns
    self.patternDict = {} # global dictionary containing all data

    # lists of all the possible components that make up a pattern
    # elevation = ['chair', 'vehicle', 'person']
    # distance = [10, 15, 20, 25]
    # direction = [0, 45, 90, 135, 180, 225, 270, 315]
    self.elevation = [0, 1, 2]
    self.distance = [0, 1, 2, 3]
    self.direction = [0, 1, 2, 3, 4, 5, 6, 7]

    # global list declarations for static patterns
    self.sRandNumList = [] # list of random numbers for static patterns
    self.visitedStaticPattern = [] # list of visited static patterns
    self.patternList = [] # list of lists containing static patterns

    # global list declarations and class initialization for dynamic patterns

    self.pat = self.dynamicPattern.pattern_builder()
    self.dRandNumList = [] # list of random numbers for dynamic patterns
    self.visitedDynamicPattern = [] # list of visited dynamic patterns
    self.dKeyList = [] # list of keys

  # create list of keys, necessary for calling dynamic patterns
    for i in self.pat:
      self.dKeyList.append(i)

  # iterate through each component to create a list of patterns
  # elevation, distance, direction
  def create_patterns(self):
    num = 0
    for i in self.elevation:
      for j in self.distance:
        for k in self.direction:
          pattern = [i, j, k]
          self.patternList.append(pattern)
          # self.patternDict['pattern list'] = self.patternList
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
        self.patternDict['visited static patterns'] = self.visitedStaticPattern
        # print(currentPattern)

    return currentPattern


  # DYNAMIC Pattern handler
  # calls dynamic_pattern_list_builder.py
  # randomly selects a dynamic pattern and calls all the beats to simulate that pattern
  # bind with "Next Dynamic button" event handler from GUI
  def dynamic_handler(self):
    dynamicPattern = Dynamic_pattern_list_builder() # initializes class to get dynamic patterns
    pat = dynamicPattern.pattern_builder() # dynamic_pattern is method to get dynamic pattern lists

    while (len(self.dRandNumList) < 23):
      rNum = random.randint(0, 22)
      while (rNum not in self.dRandNumList):
        self.dRandNumList.append(rNum)
        currentPattern = self.dKeyList[rNum]
        self.visitedDynamicPattern.append(currentPattern)
        self.patternDict['visited dynamic patterns'] = self.visitedDynamicPattern

    return currentPattern


  # keep track of participants answers
  # radio button presses will be read in and saved 
  def user_response(self):
    incorrect_response = ['chair', 10, 315] # comes from radiobuttons
    user_static_response = []
    user_response.append(incorrect_response)
    self.patternDict['user response'] = user_response

  # write to JSON
  # visited dynamic patterns, visited static patterns, current pattern, user response
  def write_data(self):
    f = open("visited.json","w")
    f.write(json.dumps(self.patternDict))
    f.close()

  # read in visited patterns
  def read_data(self):
    f = open('userData.json', 'r')
    fin = json.load(f)
    f.close()

# repopulates the lists with data written to the json file
    for i in fin:
      self.visitedStaticPattern.append(fin['visited static patterns'])
      self.user_static_response.append(fin['user static response'])
      self.visitedDynamicPattern.append(fin['visited dynamic patterns'])
      self.user_dynamic_response.append(fin['user dynamic response'])

      self.patternDict['visited static patterns'] = visitedStaticPatterns
      self.patternDict['user static response'] = userStaticResponse
      self.patternDict['visited dynamic patterns'] = visitedDynamicPattern
      self.patternDict['userDynamicResponse'] = userDynamicResponse
      print(self.patternDict)


if __name__ == '__main__':
  dPattern = Complete_hapwrap_handler()
  print ("Press CTRL c to quit")
  
  try:
    dPattern.create_patterns()
    dPattern.static_handler()
    dPattern.dynamic_handler()
    dPattern.user_response()
    dPattern.write_data()
    test2 = dPattern.read_data()
    # print(test2)

  except KeyboardInterrupt:
    print 'Interrupted'
    try:
      sys.exit(0)
    except SystemExit:
      sys.exit(0)
