#!/usr/bin/python3

import sys
import os
import json
import random
import math
from pip._vendor.webencodings.mklabels import generate

#class DataHandler:
    
currentDistance = 0
repeatCounter = 0
ctr = 0
distCtr ={'1': 0, '2': 0, '3': 0,'4': 0, '5': 0} #counter
visitedDistances = [] #list of distances used
userResponses = [] #responses

distanceDict={}

def generate_distance(): #randomly chooses distance 1-5 
    global visitedDistances
    global currentDistance
    
    distanceGenerated = False
    if(all(value == 3 for value in distCtr.values()) == True):
        print("all distances used 3 times")
        distanceGenerated = True
        
    while(distanceGenerated == False):
        randDist = random.randint(1,5)
        rand = str(randDist)
        while(distCtr[rand] != 3):
            #print(rand)
            currentDistance = randDist
            visitedDistances.append(randDist)
            #update counter
            distCtr[rand] += 1
            ctr = distCtr[rand]
            distanceGenerated = True
            
        distanceDict["visited distances"] = visitedDistances
        distanceDict["current distance"] = currentDistance
        distanceDict["counter"] = ctr  
        print(currentDistance)
        print(ctr)
        f = open('userData.json', 'w')
        f.write(json.dumps(distanceDict, sort_keys = True, indent = 1))
        f.close()
    
def save_results(): #saving study results after user inputs a file
    

    #hard coding filename , user response and repeat counter in for testing
    fileName = "fileName"
    distanceDict["user response"] = "user response here"
    distanceDict["repeat counter"] = 1
    
    fileChoice = fileName.get()
    file = open('userData.json', 'r')
    fin = json.load(file)
    file.close()
    
    distanceStats = zip(fin.get('counter'), fin.get('visited distances'), fin.get('user response'), fin.get('repeat counter'))
    
    cwd = os.getcwd()
    path_to_file = pjoin(cwd, 'completedStudies', fileChoice)
    f = open(path_to_file, "w+")
    
    f.write("Counter|Distance|User Response|Times Repeated\n")
    for i in distanceStats:
        f.write(str(i) + "\n")


generate_distance()
