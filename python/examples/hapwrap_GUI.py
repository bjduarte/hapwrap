from tkinter import *
from tkinter import ttk
import sys
import random

Root=Tk()
RTitle=Root.title("HapWrap")
RWidth=Root.winfo_screenwidth()
RHeight=Root.winfo_screenheight()
Root.geometry(("%dx%d")%(RWidth,RHeight))

#create variable for button selection
patternNum = IntVar()
buttonSpacing = IntVar()
distanceChoice = IntVar()
directionChoice = IntVar()
elevationChoice = IntVar()
numGenerated = BooleanVar()

#nitialize variables
buttonSpacing = 0
patternNum = 0
distanceChoice.set(20)
directionChoice.set(20)
elevationChoice.set(20)

#button options
elevations = [("Person",1), ("Vehicle",2), ("Chair",3)]        
distances = [("10 feet",1), ("15 feet",2), ("20 feet",3), ("25 feet",4)]        
directions = [("0°",1), ("45°",2), ("90°",3), ("135°",4), ("180°",5), ("225°",6), ("270°",7), ("315°",8)]


# lists of all the possible components that make up a pattern
# elevation = ['chair', 'vehicle', 'person']
elevation = [0, 1, 2]
distance = [0, 1, 2, 3]
# distance = [10, 15, 20, 25]
# direction = [0, 45, 90, 135, 180, 225, 270, 315]
direction = [0, 1, 2, 3, 4, 5, 6, 7]

#Display button selection 

randNumList = []
visitedPattern = []

# dictionary containning all static patterns
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
      patternDict['pattern list'] = patternList
      num += 1

def nextClick(): 

    #create elevation buttons
    nextButton.configure(state=DISABLED)
    numGenerated = False
    buttonSpacing = 0
    global patternNum
    patternNum = patternNum + 1
    statusMessage = Label(Root, height=1, width=15, text="Status: UNSAVED")
    statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight - 110, anchor=CENTER)

    # generates a random number and calls a pattern
    # tries to check for duplicate random numbers
    # we will remove the while loop and replace with "next button" event handler from GUI
    if (patternNum < 49 ):
        while numGenerated == False:
            rNum = random.randint(0, 95)
            while (rNum not in randNumList):
                randNumList.append(rNum)
                currentPattern = patternList[rNum]
                visitedPattern.append(currentPattern)
                patternDict['visited patterns'] = visitedPattern
                print(currentPattern)
                numGenerated = True

        for text, elevation in elevations:
            elevationButton = ttk.Radiobutton(Root, text=text, variable=elevationChoice, value=elevation, width = 15)
            buttonSpacing = buttonSpacing + 30
            elevationButton.place(x=RWidth/4, y=(RHeight/3) + 5 + buttonSpacing, anchor=CENTER)
            #create clearElevation button
        clearElevationButton = ttk.Button(Root, text = "Clear", command=clearElevationSelection, width = 15)
        clearElevationButton.place(x=RWidth/4, y=(RHeight/3) + 5 + 120, anchor=CENTER)

        #create distance buttons
        buttonSpacing = 0
        for text, distance in distances:
            distanceButton = ttk.Radiobutton(Root, text=text, variable=distanceChoice, value=distance, width = 15)
            buttonSpacing = buttonSpacing + 30
            distanceButton.place(x=2*RWidth/4, y=(RHeight/3) + 5 + buttonSpacing, anchor=CENTER) 
        #create clearDirection button
        clearDirectionButton = ttk.Button(Root, text = "Clear", command=clearDirectionSelection, width = 15)
        clearDirectionButton.place(x=3*RWidth/4, y=(RHeight/3) + 5 + 270, anchor=CENTER)

        #create direction buttons
        buttonSpacing = 0
        for text, direction in directions:
            directionButton = ttk.Radiobutton(Root, text=text, variable=directionChoice, value=direction, width = 15)
            buttonSpacing = buttonSpacing + 30
            directionButton.place(x=3*RWidth/4, y=(RHeight/3) + 5 + buttonSpacing, anchor=CENTER)    
        #create clearDistance button
        clearDistanceButton = ttk.Button(Root, text = "Clear", command=clearDistanceSelection, width = 15)
        clearDistanceButton.place(x=2*RWidth/4, y=(RHeight/3) + 5 + 150, anchor=CENTER)

    #create pattern text to display current pattern 
    if (patternNum < 49):
        patternMessage = Label(Root, height=1, width=25, text="Pattern " + str(patternNum))
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 110, anchor=CENTER)
        currentPatternMessage = Label(Root, height=10, width=25, text="Current Pattern:\n\tElevation = " + str(elevations[currentPattern[1]][0]) + "\n\tDistance = " + str(distances[currentPattern[2]][0]) + "\n\tDirection = " + str(directions[currentPattern[3]][0]))
        currentPatternMessage.place(x=19*RWidth/40, y=RHeight - 150, anchor=CENTER)        

    if (patternNum == 49):
        patternMessage = Label(Root, height=1, width=25, text="All 48 patterns have been done")
        patternMessage.place(x=RWidth - RWidth/7, y=RHeight - 110, anchor=CENTER)

    #set the elevation, direction, and distance radiobuttons outside their range so it appears cleared each time new pattern generated
    elevationChoice.set(20)
    directionChoice.set(20)
    distanceChoice.set(20)

def saveClick():
    if (patternNum < 49 ):
        nextButton.configure(state=NORMAL)
    else:
        saveButton.configure(state=DISABLED)

    # keep track of participants answers
    # radio button presses will be read in and saved 
    try: incorrect_response = [elevations[elevationChoice.get() - 1][0], distances[distanceChoice.get() - 1][0], directions[directionChoice.get() - 1][0]]
    except IndexError: 
        try:incorrect_response = [elevations[elevationChoice.get() - 1][0], distances[distanceChoice.get() - 1][0],0]
        except IndexError: 
            try: incorrect_response = [0, distances[distanceChoice.get() - 1][0], directions[directionChoice.get() - 1][0]]
            except IndexError: 
                    try: incorrect_response = [elevations[elevationChoice.get() - 1][0], 0, directions[directionChoice.get() - 1][0]]
                    except IndexError:
                        try: incorrect_response = [elevations[elevationChoice.get() - 1][0], 0, 0]
                        except IndexError:
                            try: [0, distances[distanceChoice.get() - 1][0], 0]
                            except IndexError:
                                try: incorrect_response = [0, 0, directions[directionChoice.get() - 1][0]]
                                except IndexError: incorrect_response = [0,0,0]

    statusMessage = Label(Root, height=1, width=15, text="Status: SAVED")
    statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight - 110, anchor=CENTER)
    print(incorrect_response)

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
elevationLabel= Label(Root, text= "Elevation:", font=("Verdana", 15))
DistanceLabel= Label(Root, text= "Distance:", height= 10, font=("Verdana", 15))
DirectionLabel= Label(Root, text= "Direction:", height= 10, font=("Verdana", 15))

#Set labels and placement
elevationLabel.place(x=RWidth/4, y=RHeight/3, anchor="center")
DistanceLabel.place(x=2*RWidth/4, y=RHeight/3, anchor="center")
DirectionLabel.place(x=3*RWidth/4, y=RHeight/3, anchor="center")

#Set screen size
size = Frame(Root, height=32, width=32)
size.pack_propagate(0) # don't shrink
size.pack()

#create Next button
nextButton = ttk.Button(Root, text='Next', command=nextClick, default='active')
nextButton.place(x=RWidth - RWidth/7, y=RHeight - 140, anchor=CENTER)

#create Save button
saveButton = ttk.Button(Root, text = "Save", command=saveClick, width = 15)
saveButton.place(x=RWidth - 2*RWidth/7, y=RHeight - 140, anchor=CENTER)

#create restore button
restoreButton = ttk.Button(Root, text = "Restore", command=restoreClick, width = 15)
restoreButton.place(x=RWidth - 5*RWidth/7, y=RHeight - 140, anchor=CENTER)

#create repeat button
repeatButton = ttk.Button(Root, text = "Repeat", command=repeatClick, width = 15)
repeatButton.place(x=RWidth - 6*RWidth/7, y=RHeight - 140, anchor=CENTER)

#create status text
statusMessage = Label(Root, height=1, width=15, text="Status: UNSAVED")
statusMessage.place(x=RWidth - 2*RWidth/7, y=RHeight - 110, anchor=CENTER)

Root.mainloop()