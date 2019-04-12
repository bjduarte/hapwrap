#!/usr/bin/python3

import sys
import os
import json
import random
import math
import array as arr

class DataHandler:
    
    #global distCtr 
    ctr = 0
    distCtr ={'1': ctr, '2': ctr, '3': ctr,'4': ctr, '5': ctr} #counter
    repeatCounter = 0
    userResponses = []
    distanceDict = {}
    visitedDistances = []
    
    #returns -1 if all distances have been used 3 times; return 1-5 for current distance generated
    def generate_distance(self): #randomly chooses distance 1-5 
        currentDistance = 0
        distanceGenerated = False
        
        #check if all distances used
        if(all(value == 3 for value in self.distCtr.values()) == True):
            print("all distances used 3 times")
            distanceGenerated = True
            return -1 #POP for file name
            #POPUP for file name

        while distanceGenerated == False:
            randDist = random.randint(1,5) #100%10)
            rand = str(randDist)
            
            #print(rand)
            ctr = self.distCtr[rand]
            #print(ctr)
            if(ctr < 4):
                #print("in loop")
                currentDistance = randDist
                self.visitedDistances.append(randDist)
                distanceGenerated = True 
                self.distCtr[rand] += 1
                ctr = self.distCtr[rand] 
        
        self.distanceDict["distance counter"] = self.distCtr
        self.distanceDict["visited distances"] = self.visitedDistances
        self.distanceDict["current distance"] = currentDistance
        #distanceDict["counter"] = ctr  
        print(currentDistance)
        return currentDistance
        
    #get user response from GUI and adds to dict
    def get_user_response(self, response):
        self.distanceDict["user response"] = response
    
    #get times repeated button is pressed from GUI and adds to dict
    def get_times_repeatbtn(self, numTimes):
        self.distanceDict["repeat counter"] = numTimes
    
    #writes data for when a new distance is being visited with the whole dictionary
    def write_to_json(self):
        f = open('userData.json', 'a+')
        f.write(json.dumps(self.distanceDict, sort_keys = True, indent = 1))
        f.close()
    
    def get_abs_or_rel(self, absOrRel):
        self.distanceDict["absolute|relative"] = absOrRel
        
    def get_prox_or_ft(self, prxOrFt):
        self.distanceDict["proximate|feet"] = proxOrFt
#saving study results after user inputs a file (fileName)
    def save_results(self, fileName): 
        fileChoice = fileName.get()
        file = open('userData.json', 'r')
        fin - json.load(file)
        file.close()

dhObject = DataHandler()
dhObject.generate_distance()
dhObject.get_user_response("no user response")
dhObject.get_times_repeatbtn(10)
dhObject.write_to_json()

