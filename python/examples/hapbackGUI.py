#!/usr/bin/python3
from appJar import gui
import datacollection as dc

#creating  class objects
dh = dc.DataHandler() #datahandler object

#This is the Entire dialog box with 1200 x 800 dimensions
app=gui("Grid Demo", "1200x800", useTtk=True)


app.setSticky("news")
app.setExpand("both")
app.setFont(20)

#Functions for the button
def press(btn):
    print(btn)

def repeat(btn):
    dh.repeatbtn()

def absolute():
    print("Entered Absolute function")
    dh.generate_distance()
    dh.get_abs_or_rel("absolute")
    dh.write_to_json()


def relative():
    print("Entered Relative function")
    dh.generate_distance()
    dh.get_abs_or_rel("relative")
    dh.write_to_json()

def prox(btn):
    dh.get_prox_or_ft("proximate")

def feet(btn):
    dh.get_prox_or_ft("feet")

def writeJson(btn):
    dh.write_to_json()

def chooseMode(btn):
    item = app.getListBox("Mode")
    print(item[0])
    a = "Absolute"
    b = "Relative"
    if item[0] == a:
        absolute()
    elif item[0] == b:
        relative()

def chooseMode(btn):
    item = app.getListBox("Mode1")
    print(item[0])
    a = "Absolute"
    b = "Relative"
    if item[0] == a:
        absolute()
    elif item[0] == b:
        relative()

def writeJsonP():
    print(app.getRadioButton("proximity1"))

def writeJsonF():
    print(app.getRadioButton("feet1"))


    
#Notebook is used for different tabs such as proximity,feet and familiarization
app.startNotebook("Notebook")

###############################################################################################################

#start of proximity tab
app.startNote("Proximity")

#all the buttons in Proximity tab- ab1,rel1 etc are the names. Absolute, relative are the titles on button
app.addListBox("Mode", ["Absolute", "Relative"],row=0,column=1,rowspan=0,colspan=0)
app.addButton("Selected",chooseMode,row=0,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity1", "Intimate",row=2,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity1", "Personal",row=3,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity1", "Social",row=4,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity1", "Public",row=5,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity1", "General Public",row=6,column=2,rowspan=0,colspan=0)
#app.addLabelOptionBox("Mode", ["- Choose one -", "Absolute", "Relative"],row=0,column=2,rowspan=0,colspan=0)
#app.addNamedButton("Absolute","ab1",absolute,row=0,column=2,rowspan=0,colspan=0)
#app.addNamedButton("Relative","rel1",relative,row=1,column=2,rowspan=0,colspan=0)

app.addNamedButton("Repeat","rep1",repeat,row=7,column=0,rowspan=0,colspan=0)
app.addNamedButton("Restore","res1",press,row=7,column=1,rowspan=0,colspan=0)

#This is just to align it properly
app.addLabel("                ",row=7,column=2,rowspan=0,colspan=0)
app.addNamedButton("Save","sav1",writeJsonP,row=7,column=3,rowspan=0,colspan=0)
app.addNamedButton("Next Pattern","nex1",press,row=7,column=4,rowspan=0,colspan=0)

# End of 1st tab
app.stopNote()

###############################################################################################################

#start of Feet tab
app.startNote("Feet")
#all the buttons in Proximity tab- ab1,rel1 etc are the names. Absolute, relative are the titles on button
app.addListBox("Mode1", ["Absolute", "Relative"],row=0,column=1,rowspan=0,colspan=0)
app.addButton("Selected ",chooseMode,row=0,column=2,rowspan=0,colspan=0)
app.addRadioButton("feet1", "5",row=2,column=2,rowspan=0,colspan=0)
app.addRadioButton("feet1", "10",row=3,column=2,rowspan=0,colspan=0)
app.addRadioButton("feet1", "15",row=4,column=2,rowspan=0,colspan=0)
app.addRadioButton("feet1", "20",row=5,column=2,rowspan=0,colspan=0)
app.addRadioButton("feet1", "25",row=6,column=2,rowspan=0,colspan=0)
#app.addLabelOptionBox("Mode", ["- Choose one -", "Absolute", "Relative"],row=0,column=2,rowspan=0,colspan=0)
#app.addNamedButton("Absolute","ab1",absolute,row=0,column=2,rowspan=0,colspan=0)
#app.addNamedButton("Relative","rel1",relative,row=1,column=2,rowspan=0,colspan=0)

app.addNamedButton("Repeat","rep2",repeat,row=7,column=0,rowspan=0,colspan=0)
app.addNamedButton("Restore","res2",press,row=7,column=1,rowspan=0,colspan=0)

#This is just to align it properly
app.addLabel("               ",row=7,column=2,rowspan=0,colspan=0)
app.addNamedButton("Save","sav2",writeJsonF,row=7,column=3,rowspan=0,colspan=0)
app.addNamedButton("Next Pattern","nex2",press,row=7,column=4,rowspan=0,colspan=0)
app.stopNote()

###############################################################################################################

#start of Familiarization tab
app.startNote("Familiarization")

#All the buttons in Proximity tab- pr2,feet2 etc are the names. Proximity and Feet are the titles on button
#The radio buttons are grouped according to the proximity group and Feet group


app.addNamedButton("  Proximity  ","pr2",press,row=0,column=1,rowspan=0,colspan=0)
app.addRadioButton("proximity", "Intimate",row=1,column=1,rowspan=0,colspan=0)
app.addRadioButton("proximity", "Personal",row=2,column=1,rowspan=0,colspan=0)
app.addRadioButton("proximity", "Social",row=3,column=1,rowspan=0,colspan=0)
app.addRadioButton("proximity", "Public",row=4,column=1,rowspan=0,colspan=0)
app.addRadioButton("proximity", "General Public",row=5,column=1,rowspan=0,colspan=0)

app.addNamedButton("  Feet  ","feet2",press,row=0,column=3,rowspan=0,colspan=0)
app.addRadioButton("feet", "5", row=1, column=3, rowspan=0, colspan=0)
app.addRadioButton("feet", "10", row=2, column=3, rowspan=0, colspan=0)
app.addRadioButton("feet", "15", row=3, column=3, rowspan=0, colspan=0)
app.addRadioButton("feet", "20", row=4, column=3, rowspan=0, colspan=0)
app.addRadioButton("feet", "25", row=5, column=3, rowspan=0, colspan=0)

app.addButton("Repeat ",repeat,row=6,column=0,rowspan=0,colspan=0)
app.addButton("Restore ",press,row=6,column=1,rowspan=0,colspan=0)
app.addLabel("              ",row=6,column=2,rowspan=0,colspan=0)
app.addButton("Save ",press,row=6,column=3,rowspan=0,colspan=0)
app.addButton("Next Pattern ",press,row=6,column=4,rowspan=0,colspan=0)
app.stopNote()

#End of the 3 tabs
app.stopNotebook()

#End of the application
app.go()
