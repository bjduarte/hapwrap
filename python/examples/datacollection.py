#!/usr/bin/python3

import sys
import os
import json
import random
import math
import array as arr
from os.path import join as pjoin
from util.button_util import *

class DataHandler:
    
    #global distCtr 
    ctr = 0
    distCtr ={'1': ctr, '2': ctr, '3': ctr,'4': ctr, '5': ctr} #counter
    repeatCounter = 0
    repeatCounterList = []
    userResponses = []
    distanceDict = {}
    visitedDistances = []
    visitedDistanceCount=[]
    #currentDistance = 0
    #returns 0 if all distances have been used 3 times; return 1-5 for current distance generated
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
       
        self.visitedDistanceCount.append(self.distCtr)
        #self.distanceDict["visited counter distances"] = self.visitedDistanceCount
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
    def repeatbtn(self):
        self.repeatCounter += 1
        self.repeatCounterList.append(self.repeatCounter)
        print("repeat")
    
    def get_abs_or_rel(self, absOrRel):
        self.distanceDict["absolute|relative mode"] = absOrRel
        
    def get_prox_or_ft(self, prxOrFt):
        self.distanceDict["proxemics|feet"] = prxOrFt
    
    #writes data for when a new distance is being visited with the whole dictionary
    def write_to_json(self):
        self.distanceDict["repeat counter"] = self.repeatCounterList
        f = open('userData.json', 'a+')
        f.write(json.dumps(self.distanceDict, sort_keys = True, indent = 1))
        f.close()
        
#saving study results after user inputs a file (fileName)
    def save_results(self, fileName): 
        
        file = open('userData.json', 'r')
        fin = json.load(file)
        file.close()
        
        saved = zip(fin.get('distance counter'),fin.get('visited distances'), fin.get('user response'), fin.get('repeat counter'))
        
        cwd = os.getcwd()
        path_to_file = pjoin(cwd, "completedStudies", fileName)
        f = open(path_to_file, "w+")
        
        f.write("Distances|User Response|Times Repeated\n")
        for i in saved:
            f.write(str(i) + "\n")  
        
        f.close()
        
#function for the restore button ?! idk what it does
    def restore(self):
        try:
            f = open('userData.json', 'r')
            fin = json.load(f)
            print(fin)
            f.close()

            for i in fin['visited distances']:
                visitedDistances.append(i)
            for i in fin['user response']:
                userResponses.append(i)
                print ("worked2")
            for i in fin['repeat counter']:
                repeatCounter.append(i)
                print ("worked3")  
            for i in fin['distance counter']:
                distCtr.append(i)     
        except:
            print("nothing to restore")
            
'''
dhObject = DataHandler()
dhObject.generate_distance()
dhObject.get_user_response("hard code: user response")
dhObject.repeatbtn()
dhObject.get_abs_or_rel("hard code: abs/res")
dhObject.get_prox_or_ft("hard code: prox/ft")
dhObject.write_to_json()
'''

