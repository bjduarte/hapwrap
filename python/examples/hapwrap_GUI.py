#!/usr/bin/python3

#from kinter import *
#from tkinter import ttk

try:
    import Tkinter as tk
except:
    import tkinter as tk
try:
    import ttk
except:
    from tkinter import ttk

from neopixel import *
import sys
import json
import random
import tkMessageBox
import shutil
import os
import time
from os import path
from complete_hapwrap_handler import *
from dynamic_pattern_list_builder import *

# LED strip configuration:
LED_COUNT = 24 # Number of LED Labels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN = 10 # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10 # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

pulse_on = Color(255, 255, 255)
pulse_off = Color(0, 0, 0)

hapwrap = Complete_hapwrap_handler()
heartbeat_pulse = 3
heartbeat_gap = 0.07 # gap between beats

try:
    Root=Tk()
except:
    Root = tk.Tk()

RTitle=Root.title("HapWrap")
RWidth=Root.winfo_screenwidth()
RHeight=Root.winfo_screenheight()
Root.geometry(("%dx%d")%(RWidth,RHeight))
 
# gives weight to the cells in the grid
rows = 0
while rows < 50:
    Root.rowconfigure(rows, weight=1)
    Root.columnconfigure(rows, weight=1)
    rows += 1
 
# Defines and places the notebook widget
eyesOnScreen = ttk.Notebook(Root)
eyesOnScreen.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
# Adds first tab of the notebook for static patterns
staticPage = ttk.Frame(eyesOnScreen)
eyesOnScreen.add(staticPage, text='Static Patterns')
 
# Adds second tab of the notebook for dynamic patterns
dynamicPage = ttk.Frame(eyesOnScreen)
eyesOnScreen.add(dynamicPage, text='Dynamic Patterns')

# Adds third tab of the notebook for familiarization
familiarizationPage = ttk.Frame(eyesOnScreen)
eyesOnScreen.add(familiarizationPage, text='Familiarization')
 

#create variable for button selection
try:
    staticPatternNum = IntVar()
except:
    staticPatternNum = tk.IntVar()    
try:
    dynamicPatternNum = IntVar()
except:
    dynamicPatternNum = tk.IntVar()
try:
    buttonSpacing = IntVar()
except:
    buttonSpacing = tk.IntVar()
try:
    distanceChoice = IntVar()
except:
    distanceChoice = tk.IntVar()
try:
    directionChoice = IntVar()
except:
    directionChoice = tk.IntVar()
try:
    elevationChoice = IntVar()
except:
    elevationChoice = tk.IntVar()
try:
    userDynamicChoice = StringVar()
except:
    userDynamicChoice = tk.StringVar()   
try:
    staticNumGenerated = BooleanVar()
except:
    staticNumGenerated = tk.BooleanVar()
try:
    dynamicNumGenerated = BooleanVar()
except:
    dynamicNumGenerated = tk.BooleanVar()    

#initialize variables
buttonSpacing = 0
staticPatternNum = 0
dynamicPatternNum = 0
dRepeatCounter = 0
sRepeatCounter = 0
checkRestoreStatic = False
checkRestoreDynamic = False
distanceChoice.set(20)
directionChoice.set(20)
elevationChoice.set(20)

#button options
elevations = [("Head Height",1), ("Chest Height",2), ("Waist Height  ",3)]        
distances = [("10 feet",1), ("15 feet",2), ("20 feet",3)]        
directions = [("0",1), ("45",2), ("90",3), ("135",4), ("180",5), ("225",6), ("270",7), ("315",8)]

# lists of all the possible components that make up a pattern
elevation = [0, 1, 2]
distance = [0, 1, 2]
direction = [0, 1, 2, 3, 4, 5, 6, 7]

#Display button selection 
dynamicPattern = Dynamic_pattern_list_builder() # initializes class to get dynamic patterns
static_incorrect_response = []
trainingPattern = []
dynamic_incorrect_response = []
randNumList = []
staticCounter = []
staticRepeatCounter = []
dynamicRepeatCounter = []
dynamicCounter = []
visitedStaticPattern = []
user_static_response = []
user_dynamic_response = []
dRandNumList = [] # list of random numbers for dynamic patterns
dKeyList = [] # list of keys
visitedDynamicPattern = [] # list of visited dynamic patterns

#dictionary containning all static patterns
patternDict = {}
#iterate through each component to create a list of patterns
#elevation, distance, direction
pat = dynamicPattern.pattern_builder()

# create list of keys, necessary for calling dynamic patterns
for i in pat:
    dKeyList.append(i)

num = 0
patternList = []
for i in elevation:
  for j in distance:
    for k in direction:
      pattern = [num, i, j, k]
      patternList.append(pattern)
      #patternDict['pattern list'] = patternList
      num += 1

# Patterns dictionary containing object positions
patterns = {
    'elevation' : [1, 2, 3],
    'distance' : [10, 15, 20], 
    'direction' : [[0, 45, 90, 135, 180, 225, 270, 315],[315, 270, 225, 180, 135, 90, 45, 0],[0, 45, 90, 135, 180, 225, 270, 315]],
    'pin_out' : [[0,1,2,3,4,5,6,7],[15, 14, 13, 12, 11, 10, 9, 8],[16,17,18,19,20,21,22,23]] }

def enterTestingPatterns(): 
    global patterns
    global pix
    global beat
    global staticPatternNum

    try: trainingPattern = [elevations[elevationChoice.get() - 1][1]-1, distances[distanceChoice.get() - 1][1]-1, directions[directionChoice.get() - 1][1]-1]
    except IndexError: 
        try: trainingPattern = [elevations[elevationChoice.get() - 1][1]-1, distances[distanceChoice.get() - 1][1]-1,0]
        except IndexError: 
            try: trainingPattern = [0, distances[distanceChoice.get() - 1][1]-1, directions[directionChoice.get() - 1][1]-1]
            except IndexError: 
                try: trainingPattern = [elevations[elevationChoice.get() - 1][1]-1, 0, directions[directionChoice.get() - 1][1]-1]
                except IndexError:
                    try: trainingPattern = [elevations[elevationChoice.get() - 1][1]-1, 0, 0]
                    except IndexError:
                        try: trainingPattern = [0, distances[distanceChoice.get() - 1][1]-1, 0]
                        except IndexError:
                            try: trainingPattern = [0, 0, directions[directionChoice.get() - 1][1]-1]
                            except IndexError: trainingPattern = [0,0,0]

    buttonSpacing = 0
    print(trainingPattern)

    pix = patterns.get('pin_out')[trainingPattern[0]][trainingPattern[2]]
    pixPointer = patterns.get('pin_out')[1][trainingPattern[2]]
    print("pix = " + str(pix))
    print("pixPointer = " + str(pixPointer))
    beat = 0

    #Heart beat code
    if (trainingPattern[1] == 0):
        beat = 0.300
    elif (trainingPattern[1] == 1):
        beat = 0.650
    elif (trainingPattern[1] == 2):
        beat = 1.000
        heart_gap = 0.5

    # Heartbeat pattern for 10 through 20 feet
    if ((trainingPattern[1] == 2) or (trainingPattern[1] == 0) or (trainingPattern[1] == 1)):
        print (trainingPattern[1])
        strip.setPixelColor(pixPointer,pulse_on)
        print ("On")
        strip.show()
        print(beat)
        time.sleep(1.0)
        
        strip.setPixelColor(pixPointer,pulse_off)
        print ("Off")
        strip.show()
        print(beat)
        time.sleep(heartbeat_gap)
        print("Beginning Heartbeat")

        print ("beat 1.0")
        for x in range(heartbeat_pulse): 
            strip.setPixelColor(pix,pulse_on)
            print ("On")
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)

            strip.setPixelColor(pix,pulse_off)
            print ("Off")
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)

            strip.setPixelColor(pix,pulse_on)
            print ("On")
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)

            strip.setPixelColor(pix,pulse_off)
            print ("Off")
            strip.show()
            print(beat)
            time.sleep(beat)

    #set the elevation, direction, and distance radiobuttons outside their range so it appears cleared each time new pattern generated
    elevationChoice.set(20)
    directionChoice.set(20)
    distanceChoice.set(20)

#function for the next button on the static page
def nextStaticClick(): 
    global patterns
    global pix
    global beat
    global rNum
    global staticPatternNum
    global sRepeatCounter
    global checkRestoreStatic

    repeatMessage = ttk.Label(staticPage, text="                                                    ")
    repeatMessage.place(x=RWidth - 6*RWidth/7, y=RHeight - 190, anchor=tk.CENTER)
    staticPatternNum = staticPatternNum + 1
    staticCounter.append(staticPatternNum)
    patternDict['user static response'] = user_static_response

    if ((staticPatternNum > 1)):
        staticRepeatCounter.append(sRepeatCounter)
        patternDict['static counter'] = staticCounter
        patternDict['Static Repeat Counter'] = staticRepeatCounter
        sRepeatCounter = 0

    if (staticPatternNum != 0):

        # keep track of participants answers
        # radio button presses will be read in and saved 
        try: static_incorrect_response = [elevations[elevationChoice.get() - 1][0], distances[distanceChoice.get() - 1][0], directions[directionChoice.get() - 1][0]]
        except IndexError: 
            try: static_incorrect_response = [elevations[elevationChoice.get() - 1][0], distances[distanceChoice.get() - 1][0],0]
            except IndexError: 
                try: static_incorrect_response = [0, distances[distanceChoice.get() - 1][0], directions[directionChoice.get() - 1][0]]
                except IndexError: 
                    try: static_incorrect_response = [elevations[elevationChoice.get() - 1][0], 0, directions[directionChoice.get() - 1][0]]
                    except IndexError:
                        try: static_incorrect_response = [elevations[elevationChoice.get() - 1][0], 0, 0]
                        except IndexError:
                            try: static_incorrect_response = [0, distances[distanceChoice.get() - 1][0], 0]
                            except IndexError:
                                try: static_incorrect_response = [0, 0, directions[directionChoice.get() - 1][0]]
                                except IndexError: static_incorrect_response = [0,0,0]
        user_static_response.append(static_incorrect_response)

    #create elevation buttons
    staticNextButton.configure(state=tk.DISABLED)
    staticNumGenerated = False
    buttonSpacing = 0

    #Each time next button is clicked status message is changed back to unsaved
    statusMessage = ttk.Label(staticPage, text="Status: UNSAVED")
    statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=tk.CENTER)

    # write patternDict to json file called userData.json
    f = open("userData.json","w")
    f.write(json.dumps(patternDict))
    f.close()

    # generates a random number and calls a pattern
    # tries to check for duplicate random numbers
    # we will remove the while loop and replace with "next button" event handler from GUI
    if (staticPatternNum < 37 ):
        while staticNumGenerated == False:
            rNum = random.randint(0, 72)
            while (rNum not in randNumList):
                randNumList.append(rNum)
                currentStaticPattern = patternList[rNum]
                visitedStaticPattern.append(currentStaticPattern)
                patternDict['visited static patterns'] = visitedStaticPattern
                staticNumGenerated = True

        pix = patterns.get('pin_out')[currentStaticPattern[1]][currentStaticPattern[3]]
        pixPointer = patterns.get('pin_out')[1][currentStaticPattern[3]]
        print(currentStaticPattern)
        print("pix = " + str(pix))
        print("pixPointer = " + str(pixPointer))
        beat = 0

        #Heart beat code
        if (distances[currentStaticPattern[2]][0] == "10 feet"):
            beat = 0.300
        elif (distances[currentStaticPattern[2]][0] == "15 feet"):
            beat = 0.650
        elif (distances[currentStaticPattern[2]][0] == "20 feet"):
            beat = 1.000
            heart_gap = 0.5

        # Heartbeat pattern for 10 through 20 feet
        if ((distances[currentStaticPattern[2]][0] == "20 feet") or (distances[currentStaticPattern[2]][0] == "10 feet") or (distances[currentStaticPattern[2]][0] == "15 feet")):
            strip.setPixelColor(pixPointer,pulse_on)
            print ("On")
            strip.show()
            print(beat)
            time.sleep(1.0)

            strip.setPixelColor(pixPointer,pulse_off)
            print ("Off")
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)
            print("Beginning Heartbeat")

            for x in range(heartbeat_pulse): 
                strip.setPixelColor(pix,pulse_on)
                print ("On")
                strip.show()
                print(beat)
                time.sleep(heartbeat_gap)

                strip.setPixelColor(pix,pulse_off)
                print ("Off")
                strip.show()
                print(beat)
                time.sleep(heartbeat_gap)

                strip.setPixelColor(pix,pulse_on)
                print ("On")
                strip.show()
                print(beat)
                time.sleep(heartbeat_gap)

                strip.setPixelColor(pix,pulse_off)
                print ("Off")
                strip.show()
                print(beat)
                time.sleep(beat)

        for text, elevation in elevations:
            elevationButton = ttk.Radiobutton(staticPage, text=text, variable=elevationChoice, value=elevation)
            buttonSpacing = buttonSpacing + 30
            elevationButton.place(x=RWidth/4, y=(RHeight/4) + 5 + buttonSpacing, anchor=tk.CENTER)
            #create clearElevation button
        clearElevationButton = ttk.Button(staticPage, text = "Clear", command=clearElevationSelection)
        clearElevationButton.place(x=RWidth/4, y=(RHeight/4) + 5 + 120, anchor=tk.CENTER)

        #create distance buttons
        buttonSpacing = 0
        for text, distance in distances:
            distanceButton = ttk.Radiobutton(staticPage, text=text, variable=distanceChoice, value=distance)
            buttonSpacing = buttonSpacing + 30
            distanceButton.place(x=2*RWidth/4, y=(RHeight/4) + 5 + buttonSpacing, anchor=tk.CENTER) 
        #create clearDistance button
        clearDistanceButton = ttk.Button(staticPage, text = "Clear", command=clearDistanceSelection)
        clearDistanceButton.place(x=2*RWidth/4, y=(RHeight/4) + 5 + 150, anchor=tk.CENTER)

        #create direction buttons
        buttonSpacing = 0
        for text, direction in directions:
            directionButton = ttk.Radiobutton(staticPage, text=text, variable=directionChoice, value=direction)
            buttonSpacing = buttonSpacing + 30
            directionButton.place(x=3*RWidth/4, y=(RHeight/4) + 5 + buttonSpacing, anchor=tk.CENTER)   
        #create clearDirection button
        clearDirectionButton = ttk.Button(staticPage, text = "Clear", command=clearDirectionSelection)
        clearDirectionButton.place(x=3*RWidth/4, y=(RHeight/4) + 5 + 270, anchor=tk.CENTER) 

    #create pattern text to display current pattern 
    if (staticPatternNum < 37):
        #dynamicNextButton.configure(state=tk.DISABLED)
        patternMessage = ttk.Label(staticPage, text="Pattern " + str(staticPatternNum))
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, anchor=tk.CENTER)

        currentStaticPatternMessage = ttk.Label(staticPage, text="Current Static Pattern:\nElevation = " + str(elevations[currentStaticPattern[1]][0]) + "\nDistance = " + str(distances[currentStaticPattern[2]][0]) + "\nDirection = " + str(directions[currentStaticPattern[3]][0]))
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, anchor=tk.CENTER)  

    if (staticPatternNum >= 37):
        patternMessage = ttk.Label(staticPage, text="Done")
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, anchor=tk.CENTER)
        currentStaticPatternMessage = ttk.Label(staticPage, text="All 36 patterns have been done")
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, anchor=tk.CENTER)  

    #set the elevation, direction, and distance radiobuttons outside their range so it appears cleared each time new pattern generated
    elevationChoice.set(20)
    directionChoice.set(20)
    distanceChoice.set(20)

    checkRestoreStatic = False

#function for the next button on the dynamic page
def nextDynamicClick(): 
    global fileName
    global dynamic_incorrect_response
    global dKeyList
    global pix
    global beat
    global dynamicPatternNum
    global currentDynamicPattern
    global dRepeatCounter
    global checkRestoreDynamic

    dynamicNextButton.configure(state=tk.DISABLED)
    dynamicNumGenerated = False
    dynamicPatternNum = dynamicPatternNum + 1
    dynamicCounter.append(dynamicPatternNum)

    repeatMessage = ttk.Label(dynamicPage, text="                                                    ")
    repeatMessage.place(x=RWidth - 6*RWidth/7, y=RHeight - 190, anchor=tk.CENTER)

    InformationMessage = ttk.Label(dynamicPage, text="Enter User Response:")
    InformationMessage.place(x=(RWidth-50)/2, y=RHeight/3 - 50, anchor=tk.CENTER) 

    dynamicUserResponse = ttk.Entry(dynamicPage, width=30, textvariable=userDynamicChoice)
    dynamicUserResponse.place(x=(RWidth-50)/2, y = RHeight/3, anchor = tk.CENTER)  

    if (dynamicPatternNum > 1 and dynamicPatternNum < 23):
        dynamicRepeatCounter.append(dRepeatCounter)
        patternDict['Dynamic Repeat Counter'] = dynamicRepeatCounter
        dRepeatCounter = 0
        #save user response when next is clicked
        dynamic_incorrect_response = userDynamicChoice.get()
        user_dynamic_response.append(dynamic_incorrect_response)
        patternDict['user dynamic response'] = user_dynamic_response
        patternDict['dynamic counter'] = dynamicCounter
        # write patternDict to json file called userData.json
        f = open("userData.json","w")
        f.write(json.dumps(patternDict))
        f.close()

    #clear the entry field
    dynamicUserResponse.delete(0,tk.END)

    if (dynamicPatternNum < 23):
        while dynamicNumGenerated == False:
            rNum = random.randint(0, 22)
            print (rNum)
            print (dKeyList) 
            while (rNum not in dRandNumList):
                dRandNumList.append(rNum)
                currentDynamicPattern = dKeyList[rNum]
                visitedDynamicPattern.append(currentDynamicPattern)
                patternDict['visited dynamic patterns'] = visitedDynamicPattern
                dynamicNumGenerated = True

        for currentBeat in pat.get(currentDynamicPattern):
            print pat.get(currentDynamicPattern)
            print currentBeat
            elevation = currentBeat[0]
            distance = currentBeat[1]
            direction = currentBeat[2]
            print ('elevation: ' + str(elevation) + ' ' + 'distance: ' + str(distance) + ' ' + 'direction: ' + str(direction))
            print (currentDynamicPattern)
            pix = patterns.get('pin_out')[elevation][direction]
            pixPointer = patterns.get('pin_out')[1][direction]
            print("pix = " + pix)
            print("pixPointer = " + pixPointer)
            beat = 0

            if (distance == 0):
                print ("distance is 0")
                beat = 0.300
            elif (distance == 1):
                print ("distance is 1")
                beat = 0.650
            elif (distance == 2):
                print ("distance is 2")
                beat = 1.000
                heart_gap = 0.5

            # Heartbeat pattern for 10 through 20 feet
            if ((distance == 2) or (distance == 1) or (distance == 0)):
              strip.setPixelColor(pixPointer,pulse_on)
              print ("On")
              strip.show()
              print(beat)
              time.sleep(1.0)

              strip.setPixelColor(pixPointer,pulse_off)
              print ("Off")
              strip.show()
              print(beat)
              time.sleep(heartbeat_gap)
              print("Beginning Heartbeat")

                for x in range(heartbeat_pulse): 
                    strip.setPixelColor(pix,pulse_on)
                    print ("On")
                    strip.show()
                    print(beat)
                    time.sleep(heartbeat_gap)

                    strip.setPixelColor(pix,pulse_off)
                    print ("Off")
                    strip.show()
                    print(beat)
                    time.sleep(heartbeat_gap)

                    strip.setPixelColor(pix,pulse_on)
                    print ("On")
                    strip.show()
                    print(beat)
                    time.sleep(heartbeat_gap)

                    strip.setPixelColor(pix,pulse_off)
                    print ("Off")
                    strip.show()
                    print(beat)
                    time.sleep(beat)
            
        #create dynamic status text
        statusMessage = ttk.Label(dynamicPage, text="Status: UNSAVED")
        statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=tk.CENTER)
        patternMessage = ttk.Label(dynamicPage, text="Pattern " + str(dynamicPatternNum))
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, anchor=tk.CENTER)
        currentStaticPatternMessage = ttk.Label(dynamicPage, text="Current Dynamic Pattern:\n" + currentDynamicPattern)
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, anchor=tk.CENTER) 

    if (dynamicPatternNum >= 24):
        fileName = ttk.Entry(dynamicPage, width=30)
        fileName.place(x=(RWidth-50)/2, y = RHeight/6, anchor = tk.CENTER)
        fileInfo = ttk.Label(dynamicPage, text="Enter a file name:")
        fileInfo.place(x=(RWidth-50)/2, y = RHeight/6 - 45, anchor = tk.CENTER)  
        fileButton = ttk.Button(dynamicPage, text="Save file", command=fileButtonClick)
        fileButton.place(x=(RWidth-50)/2 + 200, y = RHeight/6, anchor = tk.CENTER)  
        dynamicSaveButton.configure(state=tk.DISABLED)
        dynamicNextButton.configure(state=tk.DISABLED)
        patternMessage = ttk.Label(dynamicPage, text="Done          ")
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, anchor=tk.CENTER)
        currentStaticPatternMessage = ttk.Label(dynamicPage, text="All 23 patterns have been done\n                                               \n                                      ")
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, anchor=tk.CENTER) 
        
        checkRestoreDynamic = False
#function for saving the study results after the user inputs a file name
def fileButtonClick():
    # fileChoice = fileName.get()
    # save_path = './completedStudies/'

    # f= open(fileChoice + ".txt","w+")

    # completeName = os.path.join(save_path, fileChoice + ".txt")         

    save_path = 'Eyes_on/python/examples/completedStudies/'
    fileChoice = fileName.get()
    completeName = os.path.join(save_path, fileChoice +".txt")         
    file1 = open(completeName, "w")
    file1.close()

    # if path.exists("userData.json"):
    #     src = path.realpath("userData.json");
    #     # rename the original file
    #     os.rename("userData.json", fileChoice + ".txt")
    #     os.rename("Eyes_on/python/examples/" + fileChoice + ".txt", "Eyes_On/python/examples/completedStudies/"  + fileChoice + ".txt")


    # else:
    #     print("ErrorError")
#save file to folder called completedStudies
    print("saved to " + fileChoice + ".txt")
    # shutil.move("Eyes_on/python/examples/" + fileChoice + ".txt", "Eyes_On/python/examples/completedStudies/"  + fileChoice + ".txt")
    tkMessageBox.showinfo("File Status", "Data stored to " + fileChoice + ".txt")

#function for the save button on the dynamic page
def dynamicSaveClick():
    if (dynamicPatternNum < 24 ):
        dynamicNextButton.configure(state=tk.NORMAL)

    statusMessage = ttk.Label(dynamicPage, text="  Status: SAVED  ")
    statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=tk.CENTER)

#function for the save button on the static page
def staticSaveClick():
    global static_incorrect_response

    if (staticPatternNum < 49 ):
        staticNextButton.configure(state=tk.NORMAL)
    else:
        staticSaveButton.configure(state=tk.DISABLED)

    statusMessage = ttk.Label(staticPage, text="  Status: SAVED  ")
    statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=tk.CENTER)

#function for the restore button on the static page
def restoreStaticClick():
    checkRestoreStatic = True
    global staticPatternNum
    staticNextButton.configure(state=tk.NORMAL)
    staticSaveButton.configure(state=tk.NORMAL)
    staticRepeatButton.configure(state=tk.NORMAL)

    try:
        f = open('userData.json', 'r')
        fin = json.load(f)
        f.close()
        #type(fin)
        for i in fin['visited static patterns']:
            visitedStaticPattern.append(i)
        for i in fin['user static response']:
            user_static_response.append(i)
        for i in fin['static counter']:
            staticCounter.append(i)
        for i in fin['Static Repeat Counter']:
            staticRepeatCounter.append(i)
        staticPatternNum = fin['static counter'][-1] - 1

    except:
            print("nothing to restore")
            tkMessageBox.showinfo("Restore", "Nothing to restore")

#function for the restore button on the dynamic page
def restoreDynamicClick():
    checkRestoreDynamic = True
    global dynamicPatternNum
    dynamicNextButton.configure(state=tk.NORMAL)
    dynamicSaveButton.configure(state=tk.NORMAL)
    dynamicRepeatButton.configure(state=tk.NORMAL)

    try:
        f = open('userData.json', 'r')
        fin = json.load(f)
        f.close()

        for i in fin['visited static patterns']:
            visitedStaticPattern.append(i)
        for i in fin['user static response']:
            user_static_response.append(i)
        for i in fin['static counter']:
            staticCounter.append(i)
        for i in fin['visited dynamic patterns']:
            visitedDynamicPattern.append(i)
        for i in fin['user dynamic response']:
            user_dynamic_response.append(i)
        for i in fin['dynamic counter']:
            dynamicCounter.append(i)
        for i in fin['Static Repeat Counter']:
            staticRepeatCounter.append(i)
        for i in fin['Dyanmic Repeat Counter']:
            dynamicRepeatCounter.append(i)
        dynamicPatternNum = fin['dynamic counter'][-1] - 1
    except:
        try:
            f = open('userData.json', 'r')
            fin = json.load(f)
            f.close()

            for i in fin['visited static patterns']:
                visitedStaticPattern.append(i)
            for i in fin['user static response']:
                user_static_response.append(i)
            for i in fin['static counter']:
                staticCounter.append(i)
            for i in fin['Static Repeat Counter']:
                staticRepeatCounter.append(i)
            dynamicPatternNum = fin['dynamic counter'][-1] - 1
        except:
            try:
                for i in fin['visited dynamic patterns']:
                    visitedDynamicPattern.append(i)
                for i in fin['user dynamic response']:
                    user_dynamic_response.append(i)
                for i in fin['dynamic counter']:
                    dynamicCounter.append(i)
                for i in fin['Dyanmic Repeat Counter']:
                    dynamicRepeatCounter.append(i)
                dynamicPatternNum = fin['dynamic counter'][-1] - 1
            except:
                print("nothing to restore")
                tkMessageBox.showinfo("Restore", "Nothing to restore")

#function for the repeat button on the Dynamic Page
def repeatDynamicClick():
    global dRepeatCounter
    dRepeatCounter = dRepeatCounter+1
    for currentBeat in pat.get(currentDynamicPattern):
        print pat.get(currentDynamicPattern)
        print currentBeat
        elevation = currentBeat[0]
        distance = currentBeat[1]
        direction = currentBeat[2]
        print ('elevation: ' + str(elevation) + ' ' + 'distance: ' + str(distance) + ' ' + 'direction: ' + str(direction))
        print (currentDynamicPattern)
        pix = patterns.get('pin_out')[elevation][direction]
        print(pix)
        beat = 0

        if (distance == 0):
            print ("distance is 0")
            beat = 0.300
        elif (distance == 1):
            print ("distance is 1")
            beat = 0.650
        elif (distance == 2):
            print ("distance is 2")
            beat = 1.000
            heart_gap = 0.5

        # # Heartbeat pattern for 10 through 20 feet
        if ((distance == 2) or (distance == 1) or (distance == 0)):
            for x in range(heartbeat_pulse): 
                strip.setPixelColor(pix,pulse_on)
                print ("On")
                strip.show()
                print(beat)
                time.sleep(heartbeat_gap)

                strip.setPixelColor(pix,pulse_off)
                print ("Off")
                strip.show()
                print(beat)
                time.sleep(heartbeat_gap)

                strip.setPixelColor(pix,pulse_on)
                print ("On")
                strip.show()
                print(beat)
                time.sleep(heartbeat_gap)

                strip.setPixelColor(pix,pulse_off)
                print ("Off")
                strip.show()
                print(beat)
                time.sleep(beat)

    repeatMessage = ttk.Label(dynamicPage, text="Pattern was repeated")
    repeatMessage.place(x=RWidth - 6*RWidth/7, y=RHeight - 190, anchor=tk.CENTER)
    dynamicRepeatCounter.append(dRepeatCounter)

def repeatStaticClick():
    global sRepeatCounter
    sRepeatCounter = sRepeatCounter + 1
    currentStaticPattern = patternList[rNum]
    staticNumGenerated = True

    pix = patterns.get('pin_out')[currentStaticPattern[1]][currentStaticPattern[3]]
    print(currentStaticPattern)
    print("pix = " + str(pix))
    beat = 0

    #Heart beat code
    if (distances[currentStaticPattern[2]][0] == "10 feet"):
        beat = 0.300
    elif (distances[currentStaticPattern[2]][0] == "15 feet"):
        beat = 0.650
    elif (distances[currentStaticPattern[2]][0] == "20 feet"):
        beat = 1.000
        heart_gap = 0.5

    print ("pattern repeated")   

    # Heartbeat pattern for 10 through 20 feet
    if ((distances[currentStaticPattern[2]][0] == "20 feet") or (distances[currentStaticPattern[2]][0] == "10 feet") or (distances[currentStaticPattern[2]][0] == "15 feet")):
        for x in range(heartbeat_pulse): 
            strip.setPixelColor(pix,pulse_on)
            print ("On")
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)

            strip.setPixelColor(pix,pulse_off)
            print ("Off")
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)

            strip.setPixelColor(pix,pulse_on)
            print ("On")
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)

            strip.setPixelColor(pix,pulse_off)
            print ("Off")
            strip.show()
            print(beat)
            time.sleep(beat)

    repeatMessage = ttk.Label(staticPage, text="Pattern was repeated")
    repeatMessage.place(x=RWidth - 6*RWidth/7, y=RHeight - 190, anchor=tk.CENTER)   

#function to deselect the elevation button
def clearElevationSelection():
    elevationChoice.set(20)

#function to deselect the direciton button
def clearDirectionSelection():
    directionChoice.set(20) 

#function to deselect the distance button
def clearDistanceSelection():
    distanceChoice.set(20)

#Create elevation Radiobuttons for familiarization page      
for text, elevation in elevations:
    elevationButton = ttk.Radiobutton(familiarizationPage, text=text, variable=elevationChoice, value=elevation)
    buttonSpacing = buttonSpacing + 30
    elevationButton.place(x=RWidth/4, y=(RHeight/4) + 5 + buttonSpacing, anchor=tk.CENTER)
    #create clearElevation button
clearElevationButton = ttk.Button(familiarizationPage, text = "Clear", command=clearElevationSelection)
clearElevationButton.place(x=RWidth/4, y=(RHeight/4) + 5 + 120, anchor=tk.CENTER)

#Create distance Radiobuttons for familiarization page      
buttonSpacing = 0
for text, distance in distances:
    distanceButton = ttk.Radiobutton(familiarizationPage, text=text, variable=distanceChoice, value=distance)
    buttonSpacing = buttonSpacing + 30
    distanceButton.place(x=2*RWidth/4, y=(RHeight/4) + 5 + buttonSpacing, anchor=tk.CENTER) 
#create clearDistance button
clearDistanceButton = ttk.Button(familiarizationPage, text = "Clear", command=clearDistanceSelection)
clearDistanceButton.place(x=2*RWidth/4, y=(RHeight/4) + 5 + 150, anchor=tk.CENTER)

#Create direction Radiobuttons for familiarization page      
buttonSpacing = 0
for text, direction in directions:
    directionButton = ttk.Radiobutton(familiarizationPage, text=text, variable=directionChoice, value=direction)
    buttonSpacing = buttonSpacing + 30
    directionButton.place(x=3*RWidth/4, y=(RHeight/4) + 5 + buttonSpacing, anchor=tk.CENTER)   
#create clearDirection button
clearDirectionButton = ttk.Button(familiarizationPage, text = "Clear", command=clearDirectionSelection)
clearDirectionButton.place(x=3*RWidth/4, y=(RHeight/4) + 5 + 270, anchor=tk.CENTER)

#Labels for staticPage
elevationLabel= ttk.Label(staticPage, text= "Elevation:", font=("Verdana", 15))
DistanceLabel= ttk.Label(staticPage, text= "Distance:", font=("Verdana", 15))
DirectionLabel= ttk.Label(staticPage, text= "Direction:", font=("Verdana", 15))

#Labels for familiarization page
elevationLabel= ttk.Label(familiarizationPage, text= "Elevation:", font=("Verdana", 15))
DistanceLabel= ttk.Label(familiarizationPage, text= "Distance:", font=("Verdana", 15))
DirectionLabel= ttk.Label(familiarizationPage, text= "Direction:", font=("Verdana", 15))

#Set labels and placement
elevationLabel.place(x=RWidth/4, y=RHeight/4, anchor="center")
DistanceLabel.place(x=2*RWidth/4, y=RHeight/4, anchor="center")
DirectionLabel.place(x=3*RWidth/4, y=RHeight/4, anchor="center")

#create Static Next button
staticNextButton = ttk.Button(staticPage, text='Next Static Pattern', command=nextStaticClick, default='active')
staticNextButton.place(x=RWidth - RWidth/7, y=RHeight - 220, anchor=tk.CENTER)
staticNextButton.configure(state=tk.DISABLED)

#create Dynamic Next button
dynamicNextButton = ttk.Button(dynamicPage, text='Next Dynamic Pattern', command=nextDynamicClick, default='active')
dynamicNextButton.place(x=RWidth - RWidth/7, y=RHeight - 220, anchor=tk.CENTER)
dynamicNextButton.configure(state=tk.DISABLED)

#create familiarization page "Enter" button
trainingNextButton = ttk.Button(familiarizationPage, text='Enter', command=enterTestingPatterns, default='active')
trainingNextButton.place(x=RWidth - RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

#create dynamic Save button
dynamicSaveButton = ttk.Button(dynamicPage, text = "Save", command=dynamicSaveClick, width = 15)
dynamicSaveButton.place(x=RWidth - 2*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)
dynamicSaveButton.configure(state=tk.DISABLED)

#create static Save button
staticSaveButton = ttk.Button(staticPage, text = "Save", command=staticSaveClick, width = 15)
staticSaveButton.place(x=RWidth - 2*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)
staticSaveButton.configure(state=tk.DISABLED)

#create dynamic restore button
restoreDynamicButton = ttk.Button(dynamicPage, text = "Restore", command=restoreDynamicClick, width = 15)
restoreDynamicButton.place(x=RWidth - 5*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

#create static restore button
restoreStaticButton = ttk.Button(staticPage, text = "Restore", command=restoreStaticClick, width = 15)
restoreStaticButton.place(x=RWidth - 5*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

#create dynamic repeat button
staticRepeatButton = ttk.Button(staticPage, text = "Repeat", command=repeatStaticClick, width = 15)
staticRepeatButton.place(x=RWidth - 6*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)
staticRepeatButton.configure(state=tk.DISABLED)

#create static repeat button
dynamicRepeatButton = ttk.Button(dynamicPage, text = "Repeat", command=repeatDynamicClick, width = 15)
dynamicRepeatButton.place(x=RWidth - 6*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)
dynamicRepeatButton.configure(state=tk.DISABLED)

 #create static status text
#statusMessage = ttk.Label(staticPage, text="Status: UNSAVED")
#statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=tk.CENTER)

 #create dynamic status text
#statusMessage = ttk.Label(dynamicPage, text="Status: UNSAVED")
#statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=tk.CENTER)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Initialize the library (must be called once before other functions).
strip.begin()
 
Root.mainloop()