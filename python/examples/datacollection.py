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
    currDistList = []
    distCtrList = []
    userResponses = []
    distanceDict = {}
    visitedDistances = []
    visitedDistanceList=[]
    absrelModeList = []
    proxftList = []    
    listOfStudy = []
    currentDistance = 0
    
    #dictionary to convert user response to integer/distance
    convertToDist = {'5': 1, 'Intimate': 1,
                     '10': 2, 'Personal': 2,
                     '15': 3, 'Social': 3,
                     '20': 4, 'Public': 4,
                     '25': 5, 'General Public': 5}
    
    #returns -1 if all distances have been used 3 times; return 1-5 for current distance generated
    def generate_distance(self): #randomly chooses distance 1-5 
        #currentDistance = []
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
            print(ctr)
            if(ctr < 3):
                #print("in loop")
                currentDistance = randDist
                self.currDistList.append([currentDistance]) #appending current distance to list
                self.visitedDistances.append(randDist)
                #print(self.visitedDistances)
                distanceGenerated = True 
                self.distCtr[rand] += 1
                ctr = self.distCtr[rand] 
        
        print(self.distCtr)       
        self.distCtrList.append(self.distCtr.copy()) #distance counter

        (self.visitedDistanceList).append((self.visitedDistances[:])) #appending new list of visited distances
        
        
        #distanceDict["counter"] = ctr  
        #print(currentDistance)
        return currentDistance
    
    #get user response from GUI and adds to dict
    def get_user_response(self, response):
        #self.distanceDict["user response"] = response
        if(self.convertToDist[response] != self.currentDistance):
            self.userResponses.append([response])
        else:
            self.userResponses.append([0])
    
    #get times repeated button is pressed from GUI and adds to dict
    def repeatbtn(self):
        self.repeatCounter += 1
    
    def get_abs_or_rel(self, absOrRel):
        self.absrelModeList.append([absOrRel])
        
    def get_prox_or_ft(self, prxOrFt):
        self.proxftList.append([prxOrFt])
    
    #writes data for when a new distance is being visited with the whole dictionary
    def write_to_json(self):

        self.distanceDict["distance counter"] = self.distCtrList
        self.distanceDict["visited distances"] = self.visitedDistanceList
        self.distanceDict["current distance"] = self.currDistList
        self.repeatCounterList.append([self.repeatCounter])
        self.distanceDict["repeat counter"] = self.repeatCounterList
        self.distanceDict["proxemics|feet"] = self.proxftList
        self.distanceDict["absolute|relative mode"] = self.absrelModeList
        self.distanceDict["user responses"] = self.userResponses

        f = open('userData.json', 'w')
        f.write(json.dumps(self.distanceDict, sort_keys = True, indent = 1))
        f.close()
        
        self.repeatCounter = 0
        
#saving study results after user inputs a file (fileName)
    def save_results(self, fileName): 
        
        file = open('userData.json', 'r')
        fin = json.load(file)
        file.close()
        
        saved = zip(fin.get('absolute|relative mode'),fin.get('current distance'), fin.get('distance counter'),
                    fin.get('proxemics|feet'), fin.get('repeat counter'), fin.get('user responses'),
                    fin.get('visited distances'))
        
        cwd = os.getcwd()
        path_to_file = pjoin(cwd, "completedStudies", fileName)
        f = open(path_to_file, "w+")
        
        f.write("absolute|relative mode | current distance | distance counter | proxemics|feet | repeat counter | user responses | visited distances\n")
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
dhObject.get_user_response("Intimate")
dhObject.repeatbtn()

dhObject.get_abs_or_rel("absolute 1")
dhObject.get_prox_or_ft("prox")
dhObject.write_to_json()

dhObject.generate_distance()
dhObject.get_user_response("5")
dhObject.repeatbtn()
dhObject.repeatbtn()
dhObject.get_abs_or_rel("relative 1")
dhObject.get_prox_or_ft("feet")
dhObject.write_to_json()
'''