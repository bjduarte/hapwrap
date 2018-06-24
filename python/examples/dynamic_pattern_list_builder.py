#!/usr/bin/python3

import json

# This builds each dynamic pattern into a dictionary of nested lists.
# Each key is a list of lists that contain each motion of the pattern
# It then writes the dictionary to json for storage and recall

dDict = {
  'personApproachesFront' : [[2, 3, 0],
[2, 2, 0],
[2, 1, 1],
[2, 0, 2],
[2, 1, 3],
[2, 2, 4],
[2, 3, 4]],

  'personApproachesRear' : [[2, 3, 4],
[2, 2, 4],
[2, 1, 3],
[2, 0, 2],
[2, 1, 1],
[2, 2, 0],
[2, 3, 0]],

  'vehicleLeftToRight' : [
[1, 3, 2],
[1, 2, 1],
[1, 1, 1],
[1, 0, 0],
[1, 1, 7],
[1, 2, 7],
[1, 3, 6]],

  'vehicleRightToLeft' : [[1, 3, 6],
[1, 2, 7],
[1, 1, 7],
[1, 0, 0],
[1, 1, 1],
[1, 2, 1],
[1, 3, 2]],

  'approachingChairFront' : [
[0, 1, 0],
[0, 0, 0],
[0, 0, 0]],

'chairOnRight' : [[0, 1, 6],
[0, 1, 7],
[0, 1, 0],
[0, 0, 0],
[0, 0, 0]],

  'chairOnLeft' : [[0, 1, 2],
[0, 1, 1],
[0, 1, 0],
[0, 0, 0],
[0, 0, 0]],

  'vehicleLeftRear' : [
[1, 3, 3],
[1, 2, 3],
[1, 1, 2],
[1, 0, 2],
[1, 1, 2],
[1, 2, 1],
[1, 3, 1]],

  'vehicleRightFront' : [[1, 3, 7],
[1, 2, 7],
[1, 1, 6],
[1, 0, 6],
[1, 1, 6],
[1, 2, 5],
[1, 3, 5]],

  'vehicleRightTurn' : [[1, 3, 3],
[1, 2, 3],
[1, 1, 2],
[1, 0, 2],
[1, 0, 1],
[1, 0, 0],
[1, 1, 7],
[1, 2, 7],
[1, 3, 6]],

  'vehicleStopped' : [[1, 3, 2],
[1, 2, 2],
[1, 1, 1],
[1, 0, 0],
[1, 0, 0],
[1, 0, 0]],

  'personLeftToRightRear' : [[2, 2, 2],
[2, 1, 2],
[2, 0, 3],
[2, 0, 4],
[2, 0, 5],
[2, 1, 6],
[2, 2, 6]],

  'personRightToLeftRear' : [[2, 2, 6],
[2, 1, 6],
[2, 0, 5],
[2, 0, 4],
[2, 0, 3],
[2, 1, 2],
[2, 2, 2]],

  'personLeftToRightFront' : [[2, 2, 2],
[2, 1, 2],
[2, 0, 1],
[2, 0, 0],
[2, 0, 7],
[2, 1, 6],
[2, 2, 6]],

  'personRightToLeftFront' : [[2, 2, 6],
[2, 1, 6],
[2, 0, 7],
[2, 0, 0],
[2, 0, 1],
[2, 1, 2],
[2, 2, 2]],

  'personGreetingRear' : [

[2, 2, 4],
[2, 1, 4],
[2, 0, 4],
[2, 0, 5],
[2, 0, 6],
[2, 0, 7],
[2, 0, 0],
[2, 0, 0],
[2, 0, 1],
[2, 0, 2],
[2, 1, 2],
[2, 2, 2]],

  'personGreetsFront' : [[2, 2, 0],
[2, 1, 0],
[2, 0, 0],
[2, 0, 0],
[2, 0, 1],
[2, 0, 2],
[2, 1, 2],
[2, 2, 2]],

  'personGreetsLeft' : [[2, 2, 2],
[2, 1, 2],
[2, 0, 2],
[2, 0, 1],
[2, 0, 0],
[2, 0, 0],
[2, 0, 7],
[2, 1, 7],
[2, 2, 7]],

  'personGreetsRight' : [[2, 2, 6],
[2, 1, 6],
[2, 0, 6],
[2, 0, 7],
[2, 0, 0],
[2, 0, 0],
[2, 0, 1],
[2, 1, 1],
[2, 2, 1]],

  'personGreets45' : [[2, 2, 1],
[2, 1, 1],
[2, 0, 1],
[2, 0, 0],
[2, 0, 0],
[2, 0, 7],
[2, 0, 6],
[2, 0, 5],
[2, 0, 4],
[2, 1, 4],
[2, 2, 4]],

  'personGreets315' : [[2, 2, 7],
[2, 1, 7],
[2, 0, 7],
[2, 0, 0],
[2, 0, 0],
[2, 0, 7],
[2, 0, 6],
[2, 0, 5],
[2, 1, 5],
[2, 2, 5]],

  'personGreets135' : [[2, 2, 3],
[2, 1, 3],
[2, 0, 3],
[2, 0, 2],
[2, 0, 1],
[2, 0, 0],
[2, 0, 0],
[2, 0, 7],
[2, 0, 6],
[2, 1, 6],
[2, 2, 6]],

  'personGreets225' : [[2, 2, 5],
[2, 1, 5],
[2, 0, 5],
[2, 0, 6],
[2, 0, 7],
[2, 0, 0],
[2, 0, 0],
[2, 0, 1],
[2, 1, 1],
[2, 2, 1]]
}

# The dictionary of dynamic patterns is written to a json file named "dynamic_pattern_list.json"
json = json.dumps(dDict)
f = open("dynamic_pattern_list.json","w")
f.write(json)
f.close()

