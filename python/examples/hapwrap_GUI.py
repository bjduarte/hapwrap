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
import time
from complete_hapwrap_handler import *
from dynamic_pattern_list_builder import *

# LED strip configuration:
LED_COUNT = 24 # Number of LED pixels.
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
 
# Adds tab 1 of the notebook
staticPage = ttk.Frame(eyesOnScreen)
eyesOnScreen.add(staticPage, text='Static Patterns')
 
# Adds tab 2 of the notebook
dynamicPage = ttk.Frame(eyesOnScreen)
eyesOnScreen.add(dynamicPage, text='Dynamic Patterns')
 

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

#nitialize variables
buttonSpacing = 0
staticPatternNum = 0
dynamicPatternNum = 0
distanceChoice.set(20)
directionChoice.set(20)
elevationChoice.set(20)

#button options
elevations = [("Person",1), ("Vehicle",2), ("Chair  ",3)]        
distances = [("10 feet",1), ("15 feet",2), ("20 feet",3), ("25 feet",4)]        
directions = [("0",1), ("45",2), ("90",3), ("135",4), ("180",5), ("225",6), ("270",7), ("315",8)]


# lists of all the possible components that make up a pattern
elevation = [0, 1, 2]
distance = [0, 1, 2, 3]
direction = [0, 1, 2, 3, 4, 5, 6, 7]


#Display button selection 
dynamicPattern = Dynamic_pattern_list_builder() # initializes class to get dynamic patterns
pat = dynamicPattern.pattern_builder() # dynamic_pattern is method to get dynamic pattern lists
static_incorrect_response = []
dynamic_incorrect_response = []
randNumList = []
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
      patternDict['pattern list'] = patternList
      num += 1

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Initialize the library (must be called once before other functions).strip.begin()

# Dictionary containing object positions
patterns = {
    'elevation' : [1, 2, 3],
    'distance' : [10, 15, 20, 25], 
    'direction' : [[0, 45, 90, 135, 180, 225, 270, 315],[315, 270, 225, 180, 135, 90, 45, 0],[0, 45, 90, 135, 180, 225, 270, 315]],
    'pin_out' : [[0,1,2,3,4,5,6,7],[8,9,10,11,12,13,14,15],[16,17,18,19,20,21,22,23]] }

def nextStaticClick(): 
    
    global patterns

    global staticPatternNum
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
                            try: [0, distances[distanceChoice.get() - 1][0], 0]
                            except IndexError:
                                try: static_incorrect_response = [0, 0, directions[directionChoice.get() - 1][0]]
                                except IndexError: static_incorrect_response = [0,0,0]
        user_static_response.append(static_incorrect_response)
    patternDict['user static response'] = user_static_response
    #create elevation buttons
    staticNextButton.configure(state=tk.DISABLED)
    staticNumGenerated = False
    buttonSpacing = 0

    staticPatternNum = staticPatternNum + 1

    #Each time next button is clicked status message is changed back to unsaved
    statusMessage = ttk.Label(staticPage, text="Status: UNSAVED")
    statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, height=1, width=15, anchor=tk.CENTER)

    # write patternDict to json file called userData.json
    f = open("userData.json","w")
    f.write(json.dumps(patternDict))
    f.close()

    # generates a random number and calls a pattern
    # tries to check for duplicate random numbers
    # we will remove the while loop and replace with "next button" event handler from GUI
    if (staticPatternNum < 49 ):
        while staticNumGenerated == False:
            rNum = random.randint(0, 95)
            while (rNum not in randNumList):
                randNumList.append(rNum)
                currentStaticPattern = patternList[rNum]
                visitedStaticPattern.append(currentStaticPattern)
                patternDict['visited static patterns'] = visitedStaticPattern
                staticNumGenerated = True

        pix = patterns.get('pin_out')[currentStaticPattern[1]-1][currentStaticPattern[3]]
        print(currentStaticPattern)
        print("pix = " + str(pix))
        beat = 0

        #Heart beat code
        if (distances[currentStaticPattern[2]][0] == "10 feet"):
            print("10 feet = beat of 0.3")
            beat = 0.300
        elif (distances[currentStaticPattern[2]][0] == "15 feet"):
            print("15 feet = beat of 0.65")
            beat = 0.650
        elif (distances[currentStaticPattern[2]][0] == "20 feet"):
            print("20 feet = beat of 1")
            beat = 1.000
        elif (distances[currentStaticPattern[2]][0] == "25 feet"):
            print("25 feet = beat of 1 and heartgap of 0.5")
            beat = 1.00
            heart_gap = 0.5

        # sonar pulse for 25 feet
        for i in range(heartbeat_pulse):
            strip.setPixelColor(pix,pulse_on)
            strip.show()
            print (beat)
            time.sleep(heart_gap)

            strip.setPixelColor(pix,pulse_off)
            strip.show()
            print(beat)
            time.sleep(beat)

        # Heartbeat pattern for 10 through 20 feet
        for x in range(heartbeat_pulse): 
            strip.setPixelColor(pix,pulse_on)
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)

            strip.setPixelColor(pix,pulse_off)
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)

            strip.setPixelColor(pix,pulse_on)
            strip.show()
            print(beat)
            time.sleep(heartbeat_gap)

            strip.setPixelColor(pix,pulse_off)
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
    if (staticPatternNum < 49):
        #dynamicNextButton.configure(state=tk.DISABLED)
        patternMessage = ttk.Label(staticPage, text="Pattern " + str(staticPatternNum))
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, height=1, width=15, anchor=tk.CENTER)

        currentStaticPatternMessage = ttk.Label(staticPage, text="Current Static Pattern:\nElevation = " + str(elevations[currentStaticPattern[1]][0]) + "\nDistance = " + str(distances[currentStaticPattern[2]][0]) + "\nDirection = " + str(directions[currentStaticPattern[3]][0]))
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, height=5, width=25, anchor=tk.CENTER)  

    if (staticPatternNum >= 49):
        patternMessage = ttk.Label(staticPage, text="Done")
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, height=1, width=25, anchor=tk.CENTER)
        currentStaticPatternMessage = ttk.Label(staticPage, text="All 48 patterns have been done")
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, height=5, width=25, anchor=tk.CENTER)  

    #set the elevation, direction, and distance radiobuttons outside their range so it appears cleared each time new pattern generated
    elevationChoice.set(20)
    directionChoice.set(20)
    distanceChoice.set(20)

def nextDynamicClick(): 
    global dynamic_incorrect_response

    dynamicNextButton.configure(state=tk.DISABLED)
    dynamicNumGenerated = False
    global dynamicPatternNum
    dynamicPatternNum = dynamicPatternNum + 1

    InformationMessage = ttk.Label(dynamicPage, text="Enter User Response:")
    InformationMessage.place(x=(RWidth-50)/2, y=RHeight/3 - 50, height=1, width=25, anchor=tk.CENTER) 

    dynamicUserResponse = ttk.Entry(dynamicPage, width=30, textvariable=userDynamicChoice)
    dynamicUserResponse.place(x=(RWidth-50)/2, y = RHeight/3, anchor = tk.CENTER)  
    
    if (dynamicPatternNum != 1 & dynamicPatternNum < 24):
        #save user response when next is clicked
        dynamic_incorrect_response = userDynamicChoice.get()
        user_dynamic_response.append(dynamic_incorrect_response)
        patternDict['user dynamic response'] = user_dynamic_response

        # write patternDict to json file called userData.json
        f = open("userData.json","w")
        f.write(json.dumps(patternDict))
        f.close()

    #clear the entry field
    dynamicUserResponse.delete(0,tk.END)

    if (dynamicPatternNum < 24):
        while dynamicNumGenerated == False:
            rNum = random.randint(0, 22)
            while (rNum not in dRandNumList):
                dRandNumList.append(rNum)
                currentDynamicPattern = dKeyList[rNum]
                visitedDynamicPattern.append(currentDynamicPattern)
                patternDict['visited dynamic patterns'] = visitedDynamicPattern
                dynamicNumGenerated = True
        #create dynamic status text
        statusMessage = ttk.Label(dynamicPage, text="Status: UNSAVED")
        statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, height=1, width=15, anchor=tk.CENTER)
        patternMessage = ttk.Label(dynamicPage, text="Pattern " + str(dynamicPatternNum))
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, height=1, width=15, anchor=tk.CENTER)
        currentStaticPatternMessage = ttk.Label(dynamicPage, text="Current Dynamic Pattern:\n" + currentDynamicPattern)
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, height=5, width=25, anchor=tk.CENTER) 

    if (dynamicPatternNum >= 24):
        dynamicSaveButton.configure(state=tk.DISABLED)
        dynamicNextButton.configure(state=tk.DISABLED)
        patternMessage = ttk.Label(dynamicPage, text="Done")
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, height=1, width=15, anchor=tk.CENTER)
        currentStaticPatternMessage = ttk.Label(dynamicPage, text="All 23 patterns have been done")
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, height=5, width=25, anchor=tk.CENTER) 
 
def dynamicSaveClick():
    if (dynamicPatternNum < 24 ):
        dynamicNextButton.configure(state=tk.NORMAL)

    statusMessage = ttk.Label(dynamicPage, text="Status: SAVED")
    statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, height=1, width=15, anchor=tk.CENTER)
def staticSaveClick():
    global static_incorrect_response

    if (staticPatternNum < 49 ):
        staticNextButton.configure(state=tk.NORMAL)
    else:
        staticSaveButton.configure(state=tk.DISABLED)

    statusMessage = ttk.Label(staticPage, text="Status: SAVED")
    statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, height=1, width=15, anchor=tk.CENTER)

def restoreClick():
    print ("patterns restored") 

def repeatClick():
    print ("pattern repeated")  

#function to deselect the elevation button
def clearElevationSelection():
    elevationChoice.set(20)

#function to deselect the direciton button
def clearDirectionSelection():
    directionChoice.set(20) 

#function to deselect the distance button
def clearDistanceSelection():
    distanceChoice.set(20)


#Labels
elevationLabel= ttk.Label(staticPage, text= "Elevation:", font=("Verdana", 15))
DistanceLabel= ttk.Label(staticPage, text= "Distance:", font=("Verdana", 15))
DirectionLabel= ttk.Label(staticPage, text= "Direction:", font=("Verdana", 15))

#Set labels and placement
elevationLabel.place(x=RWidth/4, y=RHeight/4, anchor="center")
DistanceLabel.place(x=2*RWidth/4, y=RHeight/4, anchor="center")
DirectionLabel.place(x=3*RWidth/4, y=RHeight/4, anchor="center")

#create Static Next button
staticNextButton = ttk.Button(staticPage, text='Next Static Pattern', command=nextStaticClick, default='active')
staticNextButton.place(x=RWidth - RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

#create Dynamic Next button
dynamicNextButton = ttk.Button(dynamicPage, text='Next Dynamic Pattern', command=nextDynamicClick, default='active')
dynamicNextButton.place(x=RWidth - RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

#create dynamic Save button
dynamicSaveButton = ttk.Button(dynamicPage, text = "Save", command=dynamicSaveClick, width = 15)
dynamicSaveButton.place(x=RWidth - 2*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

#create static Save button
staticSaveButton = ttk.Button(staticPage, text = "Save", command=staticSaveClick, width = 15)
staticSaveButton.place(x=RWidth - 2*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

#create dynamic restore button
restoreButton = ttk.Button(dynamicPage, text = "Restore", command=restoreClick, width = 15)
restoreButton.place(x=RWidth - 5*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

#create static restore button
restoreButton = ttk.Button(staticPage, text = "Restore", command=restoreClick, width = 15)
restoreButton.place(x=RWidth - 5*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

#create dynamic repeat button
repeatButton = ttk.Button(dynamicPage, text = "Repeat", command=repeatClick, width = 15)
repeatButton.place(x=RWidth - 6*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

#create static repeat button
repeatButton = ttk.Button(staticPage, text = "Repeat", command=repeatClick, width = 15)
repeatButton.place(x=RWidth - 6*RWidth/7, y=RHeight - 220, anchor=tk.CENTER)

 #create static status text
statusMessage = ttk.Label(staticPage, text="Status: UNSAVED")
statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, height=1, width=15, anchor=tk.CENTER)

 #create dynamic status text
statusMessage = ttk.Label(dynamicPage, text="Status: UNSAVED")
statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, height=1, width=15, anchor=tk.CENTER)
 
Root.mainloop()