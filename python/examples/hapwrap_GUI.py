from tkinter import *
from tkinter import ttk
from dynamic_pattern_list_builder import *
import sys
import json
import random

Root=Tk()
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
staticPatternNum = IntVar()
dynamicPatternNum = IntVar()
buttonSpacing = IntVar()
distanceChoice = IntVar()
directionChoice = IntVar()
elevationChoice = IntVar()
userDynamicChoice = StringVar()
staticNumGenerated = BooleanVar()
dynamicNumGenerated = BooleanVar()

#nitialize variables
buttonSpacing = 0
staticPatternNum = 0
dynamicPatternNum = 0
distanceChoice.set(20)
directionChoice.set(20)
elevationChoice.set(20)

#button options
elevations = [("Person",1), ("Vehicle",2), ("Chair",3)]        
distances = [("10 feet",1), ("15 feet",2), ("20 feet",3), ("25 feet",4)]        
directions = [("0°",1), ("45°",2), ("90°",3), ("135°",4), ("180°",5), ("225°",6), ("270°",7), ("315°",8)]


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
elevation, distance, direction

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

def nextStaticClick(): 

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
    staticNextButton.configure(state=DISABLED)
    staticNumGenerated = False
    buttonSpacing = 0

    staticPatternNum = staticPatternNum + 1

    #Each time next button is clicked status message is changed back to unsaved
    statusMessage = Label(staticPage, height=1, width=15, text="Status: UNSAVED")
    statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=CENTER)

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

        for text, elevation in elevations:
            elevationButton = ttk.Radiobutton(staticPage, text=text, variable=elevationChoice, value=elevation)
            buttonSpacing = buttonSpacing + 30
            elevationButton.place(x=RWidth/4, y=(RHeight/4) + 5 + buttonSpacing, anchor=CENTER)
            #create clearElevation button
        clearElevationButton = ttk.Button(staticPage, text = "Clear", command=clearElevationSelection)
        clearElevationButton.place(x=RWidth/4, y=(RHeight/4) + 5 + 120, anchor=CENTER)

        #create distance buttons
        buttonSpacing = 0
        for text, distance in distances:
            distanceButton = ttk.Radiobutton(staticPage, text=text, variable=distanceChoice, value=distance)
            buttonSpacing = buttonSpacing + 30
            distanceButton.place(x=2*RWidth/4, y=(RHeight/4) + 5 + buttonSpacing, anchor=CENTER) 
        #create clearDistance button
        clearDistanceButton = ttk.Button(staticPage, text = "Clear", command=clearDistanceSelection)
        clearDistanceButton.place(x=2*RWidth/4, y=(RHeight/4) + 5 + 150, anchor=CENTER)

        #create direction buttons
        buttonSpacing = 0
        for text, direction in directions:
            directionButton = ttk.Radiobutton(staticPage, text=text, variable=directionChoice, value=direction)
            buttonSpacing = buttonSpacing + 30
            directionButton.place(x=3*RWidth/4, y=(RHeight/4) + 5 + buttonSpacing, anchor=CENTER)   
        #create clearDirection button
        clearDirectionButton = ttk.Button(staticPage, text = "Clear", command=clearDirectionSelection)
        clearDirectionButton.place(x=3*RWidth/4, y=(RHeight/4) + 5 + 270, anchor=CENTER) 

    #create pattern text to display current pattern 
    if (staticPatternNum < 49):
        #dynamicNextButton.configure(state=DISABLED)
        patternMessage = Label(staticPage, height=1, width=15, text="Pattern " + str(staticPatternNum))
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, anchor=CENTER)

        currentStaticPatternMessage = Label(staticPage, height=5, width=25, text="Current Static Pattern:\nElevation = " + str(elevations[currentStaticPattern[1]][0]) + "\nDistance = " + str(distances[currentStaticPattern[2]][0]) + "\nDirection = " + str(directions[currentStaticPattern[3]][0]))
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, anchor=CENTER)  

    if (staticPatternNum >= 49):
        patternMessage = Label(staticPage, height=1, width=25, text="Done")
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, anchor=CENTER)
        currentStaticPatternMessage = Label(staticPage, height=5, width=25, text="All 48 patterns have been done")
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, anchor=CENTER)  

    #set the elevation, direction, and distance radiobuttons outside their range so it appears cleared each time new pattern generated
    elevationChoice.set(20)
    directionChoice.set(20)
    distanceChoice.set(20)

def nextDynamicClick(): 
    global dynamic_incorrect_response

    dynamicNextButton.configure(state=DISABLED)
    dynamicNumGenerated = False
    global dynamicPatternNum
    dynamicPatternNum = dynamicPatternNum + 1

    InformationMessage = Label(dynamicPage, height=1, width=15, text="Enter User Response:")
    InformationMessage.place(x=(RWidth-50)/2, y=RHeight/3 - 50, anchor=CENTER) 

    dynamicUserResponse = ttk.Entry(dynamicPage, width=30, textvariable=userDynamicChoice)
    dynamicUserResponse.place(x=(RWidth-50)/2, y = RHeight/3, anchor = CENTER)  
    
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
    dynamicUserResponse.delete(0,END)

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
        statusMessage = Label(dynamicPage, height=1, width=15, text="Status: UNSAVED")
        statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=CENTER)
        patternMessage = Label(dynamicPage, height=1, width=15, text="Pattern " + str(dynamicPatternNum))
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, anchor=CENTER)
        currentStaticPatternMessage = Label(dynamicPage, height=5, width=25, text="Current Dynamic Pattern:\n" + currentDynamicPattern)
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, anchor=CENTER) 

    if (dynamicPatternNum >= 24):
        dynamicSaveButton.configure(state=DISABLED)
        dynamicNextButton.configure(state=DISABLED)
        patternMessage = Label(dynamicPage, height=1, width=15, text="Done")
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 190, anchor=CENTER)
        currentStaticPatternMessage = Label(dynamicPage, height=5, width=25, text="All 23 patterns have been done")
        currentStaticPatternMessage.place(x=19*RWidth/40, y=RHeight - 200, anchor=CENTER) 
 
def dynamicSaveClick():
    if (dynamicPatternNum < 24 ):
        dynamicNextButton.configure(state=NORMAL)

    statusMessage = Label(dynamicPage, height=1, width=15, text="Status: SAVED")
    statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=CENTER)
def staticSaveClick():
    global static_incorrect_response

    if (staticPatternNum < 49 ):
        staticNextButton.configure(state=NORMAL)
    else:
        staticSaveButton.configure(state=DISABLED)

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
elevationLabel= Label(staticPage, text= "Elevation:", font=("Verdana", 15))
DistanceLabel= Label(staticPage, text= "Distance:", font=("Verdana", 15))
DirectionLabel= Label(staticPage, text= "Direction:", font=("Verdana", 15))

#Set labels and placement
elevationLabel.place(x=RWidth/4, y=RHeight/4, anchor="center")
DistanceLabel.place(x=2*RWidth/4, y=RHeight/4, anchor="center")
DirectionLabel.place(x=3*RWidth/4, y=RHeight/4, anchor="center")

#create Static Next button
staticNextButton = ttk.Button(staticPage, text='Next Static Pattern', command=nextStaticClick, default='active')
staticNextButton.place(x=RWidth - RWidth/7, y=RHeight - 220, anchor=CENTER)

#create Dynamic Next button
dynamicNextButton = ttk.Button(dynamicPage, text='Next Dynamic Pattern', command=nextDynamicClick, default='active')
dynamicNextButton.place(x=RWidth - RWidth/7, y=RHeight - 220, anchor=CENTER)

#create dynamic Save button
dynamicSaveButton = ttk.Button(dynamicPage, text = "Save", command=dynamicSaveClick, width = 15)
dynamicSaveButton.place(x=RWidth - 2*RWidth/7, y=RHeight - 220, anchor=CENTER)

#create static Save button
staticSaveButton = ttk.Button(staticPage, text = "Save", command=staticSaveClick, width = 15)
staticSaveButton.place(x=RWidth - 2*RWidth/7, y=RHeight - 220, anchor=CENTER)

#create dynamic restore button
restoreButton = ttk.Button(dynamicPage, text = "Restore", command=restoreClick, width = 15)
restoreButton.place(x=RWidth - 5*RWidth/7, y=RHeight - 220, anchor=CENTER)

#create static restore button
restoreButton = ttk.Button(staticPage, text = "Restore", command=restoreClick, width = 15)
restoreButton.place(x=RWidth - 5*RWidth/7, y=RHeight - 220, anchor=CENTER)

#create dynamic repeat button
repeatButton = ttk.Button(dynamicPage, text = "Repeat", command=repeatClick, width = 15)
repeatButton.place(x=RWidth - 6*RWidth/7, y=RHeight - 220, anchor=CENTER)

#create static repeat button
repeatButton = ttk.Button(staticPage, text = "Repeat", command=repeatClick, width = 15)
repeatButton.place(x=RWidth - 6*RWidth/7, y=RHeight - 220, anchor=CENTER)

 #create static status text
statusMessage = Label(staticPage, height=1, width=15, text="Status: UNSAVED")
statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=CENTER)

 #create dynamic status text
statusMessage = Label(dynamicPage, height=1, width=15, text="Status: UNSAVED")
statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=CENTER)
 
Root.mainloop()