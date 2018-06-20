#!/usr/bin/python3

import json
import io
import random

# lists of all the possible components that make up a pattern
elevation = ['chair', 'vehicle', 'person']
distance = [10, 15, 20, 25]
direction = [0, 45, 90, 135, 180, 225, 270, 315]
visitedPattern = []


# iterate through each component to create a list of patterns
# elevation, distance, direction
num = 0
patternList = []
for i in elevation:
  for j in distance:
    for k in direction:
      pattern = [num, i, j, k]
      patternList.append(pattern)
      num += 1

# generates a random number and calls a pattern
# tries to check for duplicate random numbers
# we will remove the while loop and replace with "next button" event handler from GUI
while (len(visitedPattern) < len(patternList)):
  rNum = random.randint(0, 95)
  while (rNum not in visitedPattern):
    visitedPattern.append(rNum)
    currentPattern = patternList[rNum]
    # print(currentPattern)

# keep track of participants answers
# radio button presses will be read in and saved 
incorrect_response = [elevation, distance, direction]
user_response = []
user_response.appepynd(incorrect_response)

# creates a dictionary to keep track of visited patterns for recall
patternDict = {
   # 'vibration pattern' : patternList,
  'visited patterns' : visitedPattern,
  'current pattern' : currentPattern,
  'user response' : user_response
}



# write to JSON
# list of patterns, randomly generated numbers for patterns, current pattern
json = json.dumps(patternDict)
f = open("visited.json","w")
f.write(json)
f.close()

# read in visited patterns
# f = open('visited.json', 'r')
# fin = json.load(f)
# f.close()
#
# for i in fin:
#     print(fin['visited patterns'])
#
