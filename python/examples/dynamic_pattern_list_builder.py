#!/usr/bin/python3

import json

# This builds each dynamic pattern into a dictionary of nested lists.
# Each key is a list of lists that contain each motion of the pattern
# It then writes the dictionary to json for storage and recall
class Dynamic_pattern_list_builder:
  
  def pattern_builder(self):
    dDict = {
      'personApproachesFront' : [
        [0, 2, 0],
        [0, 1, 1],
        [0, 0, 2],
        [0, 1, 3],
        [0, 2, 4]],

      'personApproachesRear' : [
[0, 2, 4],
[0, 1, 3],
[0, 0, 2],
[0, 1, 1],
[0, 2, 0]],

      'vehicleLeftToRight' : [
[1, 2, 7],
[1, 1, 7],
[1, 0, 0],
[1, 1, 1],
[1, 2, 1]],

      'vehicleRightToLeft' : [
[1, 2, 1],
[1, 1, 1],
[1, 0, 0],
[1, 1, 7],
[1, 2, 7]],

      'approachingChairFront' : [
[2, 1, 0],
[2, 0, 0],
[2, 0, 0]],

    'chairOnLeft' : [
[2, 1, 6],
[2, 1, 7],
[2, 1, 0],
[2, 0, 0],
[2, 0, 0]],

      'chairOnRight' : [
[2, 1, 2],
[2, 1, 1],
[2, 1, 0],
[2, 0, 0],
[2, 0, 0]],

      'vehicleLeftRear' : [
[1, 2, 5],
[1, 1, 6],
[1, 0, 6],
[1, 1, 6],
[1, 2, 7]],

      'vehicleRightFront' : [
[1, 2, 1],
[1, 1, 2],
[1, 0, 2],
[1, 1, 2],
[1, 2, 3]],

      'vehicleRightTurn' : [
[1, 2, 5],
[1, 1, 6],
[1, 0, 6],
[1, 0, 7],
[1, 0, 0],
[1, 1, 1],
[1, 2, 1]],

      'vehicleStopped' : [
[1, 2, 6],
[1, 1, 7],
[1, 0, 0],
[1, 0, 0]],

      'personRightToLeftRear' : [
[0, 2, 2],
[0, 1, 2],
[0, 0, 3],
[0, 0, 4],
[0, 0, 5],
[0, 1, 6],
[0, 2, 6]],

      'personLeftToRightRear' : [
[0, 2, 6],
[0, 1, 6],
[0, 0, 5],
[0, 0, 4],
[0, 0, 3],
[0, 1, 2],
[0, 2, 2]],

      'personRightToLeftFront' : [
[0, 2, 2],
[0, 1, 2],
[0, 0, 1],
[0, 0, 0],
[0, 0, 7],
[0, 1, 6],
[0, 2, 6]],

      'personLeftToRightFront' : [
[0, 2, 6],
[0, 1, 6],
[0, 0, 7],
[0, 0, 0],
[0, 0, 1],
[0, 1, 2],
[0, 2, 2]],

      'personGreetingRear' : [
[0, 2, 4],
[0, 1, 4],
[0, 0, 4],
[0, 0, 5],
[0, 0, 6],
[0, 0, 7],
[0, 0, 0],
[0, 0, 0],
[0, 0, 1],
[0, 0, 2],
[0, 1, 2],
[0, 2, 2]],

      'personGreetsFront' : [
[0, 2, 0],
[0, 1, 0],
[0, 0, 0],
[0, 0, 0],
[0, 0, 1],
[0, 0, 2],
[0, 1, 2],
[0, 2, 2]],

      'personGreetsRight' : [
[0, 2, 2],
[0, 1, 2],
[0, 0, 2],
[0, 0, 1],
[0, 0, 0],
[0, 0, 0],
[0, 0, 7],
[0, 1, 7],
[0, 2, 7]],

      'personGreetsLeft' : [
[0, 2, 6],
[0, 1, 6],
[0, 0, 6],
[0, 0, 7],
[0, 0, 0],
[0, 0, 0],
[0, 0, 1],
[0, 1, 1],
[0, 2, 1]],

      'personGreets45' : [
[0, 2, 1],
[0, 1, 1],
[0, 0, 1],
[0, 0, 0],
[0, 0, 0],
[0, 0, 7],
[0, 0, 6],
[0, 0, 5],
[0, 0, 4],
[0, 1, 4],
[0, 2, 4]],

      'personGreets315' : [
        [0, 2, 7],
        [0, 1, 7],
        [0, 0, 7],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 7],
        [0, 0, 6],
        [0, 0, 5],
        [0, 1, 5],
        [0, 2, 5]],

      'personGreets135' : [
[0, 2, 3],
[0, 1, 3],
[0, 0, 3],
[0, 0, 2],
[0, 0, 1],
[0, 0, 0],
[0, 0, 0],
[0, 0, 7],
[0, 0, 6],
[0, 1, 6],
[0, 2, 6]],

      'personGreets225' : [
[0, 2, 5],
[0, 1, 5],
[0, 0, 5],
[0, 0, 6],
[0, 0, 7],
[0, 0, 0],
[0, 0, 0],
[0, 0, 1],
[0, 1, 1],
[0, 2, 1]]
    }
    return dDict
  # The dictionary of dynamic patterns is written to a json file named "dynamic_pattern_list.json"
  def write_patterns():
    json = json.dumps(dDict)
    f = open("dynamic_pattern_list.json","w")
    f.write(json)
    f.close()

