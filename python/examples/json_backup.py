#!/usr/bin/python3

import json
import io
import random

# lists of all the possible components that make up a pattern
elevation = ['chair', 'vehicle', 'person']
distance = [10, 15, 20, 25]
direction = [0, 45, 90, 135, 180, 225, 270, 315]
randNumList = []
visitedPattern = []

# dictionary of all data
patternDict = {}


# iterate through each component to create a list of patterns
# elevation, distance, direction
num = 0
patternList = []
for i in elevation:
  for j in distance:
    for k in direction:
      pattern = [num, i, j, k]
      patternList.append(pattern)
      # patternDict['pattern list'] = patternList
      num += 1

# generates a random number and calls a pattern
# tries to check for duplicate random numbers
# we will remove the while loop and replace with "next button" event handler from GUI
while (len(randNumList) < 48):
  rNum = random.randint(0, 48)
  while (rNum not in randNumList):
    randNumList.append(rNum)
    currentPattern = patternList[rNum]
    visitedPattern.append(currentPattern)
    patternDict['visited patterns'] = visitedPattern
    print(currentPattern)


# keep track of participants answers
# radio button presses will be read in and saved 
incorrect_response = [elevation, distance, direction]
user_response = []
user_response.append(incorrect_response)
patternDict['user response'] = user_response

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
#     print(fin['visited patterns'], fin['user response'])

