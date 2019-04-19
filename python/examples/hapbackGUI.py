#!/usr/bin/python3
from appJar import gui
import datacollection as dc
from util.button_util import ButtonType
from typing import Dict

#creating  class objects
dh = dc.DataHandler() #datahandler object

#This is the Entire dialog box with 1200 x 800 dimensions
app=gui("Grid Demo", "1200x800", useTtk=True)

# variables to keep track of familiarization radio buttons hit
fam_state_feet: str = '5'
fam_state_prox: str = 'Intimate'
fam_test_state: str = 'absolute_1'


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

def restore():
    dh.restore()

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

def change_fam_state(btn) -> None:
    global fam_state_feet, fam_state_prox, fam_test_state
    if btn is 'feet':
        fam_state_feet = app.getRadioButton('feet')
        print(f'feet state is: {fam_state_feet}')
    elif btn is 'proximity':
        fam_state_prox = app.getRadioButton('proximity')
        print(f'prox state is: {fam_state_prox}')
    elif btn is 'test_state':
        fam_test_state = app.getRadioButton('test_state')
        print(f'test state is: {fam_test_state}')


def fam_press(btn) -> None:
    global fam_state_feet, fam_state_prox
    if btn is 'feet2':
        fam_pattern = fam_state_feet + f'_{fam_test_state}'
        print(f'vibrating for {fam_pattern}')
        api_feet_call_dict: Dict = {'5_absolute_1': [ButtonType.feet_abs.get_api_call, 0, 0,],
                                    '5_relative_1': [ButtonType.feet_rel.get_api_call, 1, 0,],
                                    '10_absolute_1':[ButtonType.feet_abs.get_api_call, 1, 0,],
                                    '10_relative_1': [ButtonType.feet_rel.get_api_call, 2, 0,],
                                    '15_absolute_1': [ButtonType.feet_abs.get_api_call, 2, 0,],
                                    '15_relative_1': [ButtonType.feet_rel.get_api_call, 3, 0,],
                                    '20_absolute_1': [ButtonType.feet_abs.get_api_call, 3, 0,],
                                    '20_relative_1': [ButtonType.feet_rel.get_api_call, 4, 0,],
                                    '25_absolute_1': [ButtonType.feet_abs.get_api_call, 4, 0,],
                                    '25_relative_1': [ButtonType.feet_rel.get_api_call, 5, 0,],
                                    '5_absolute_2': [ButtonType.feet_abs.get_api_call, 0, 1,],
                                    '5_relative_2': [ButtonType.feet_rel.get_api_call, 1, 1,],
                                    '10_absolute_2': [ButtonType.feet_abs.get_api_call, 1, 1,],
                                    '10_relative_2': [ButtonType.feet_rel.get_api_call, 2, 1,],
                                    '15_absolute_2': [ButtonType.feet_abs.get_api_call, 2, 1,],
                                    '15_relative_2': [ButtonType.feet_rel.get_api_call, 3, 1,],
                                    '20_absolute_2': [ButtonType.feet_abs.get_api_call, 3, 1,],
                                    '20_relative_2': [ButtonType.feet_rel.get_api_call, 4, 1,],
                                    '25_absolute_2': [ButtonType.feet_abs.get_api_call, 4, 1,],
                                    '25_relative_2': [ButtonType.feet_rel.get_api_call, 5, 1,]
                                    }

        print(f'{api_feet_call_dict[fam_pattern][1]}, {api_feet_call_dict[fam_pattern][2]}')
        api_feet_call_dict[fam_pattern][0](api_feet_call_dict[fam_pattern][1],
                                           api_feet_call_dict[fam_pattern][2])
        print(f'finished vibrating for {fam_state_feet}')

    if btn is 'pr2':
        print(f'vibrating for {fam_state_prox}')
        fam_pattern = fam_state_prox + f'_{fam_test_state}'
        api_prox_call_dict: Dict = {'Intimate_absolute_1': [ButtonType.prox_abs.get_api_call, 0, 0],
                                    'Intimate_relative_1': [ButtonType.prox_rel.get_api_call, 1, 0],
                                    'Personal_absolute_1': [ButtonType.prox_abs.get_api_call, 1, 0],
                                    'Personal_relative_1': [ButtonType.prox_rel.get_api_call, 2, 0],
                                    'Social_absolute_1': [ButtonType.prox_abs.get_api_call, 2, 0],
                                    'Social_relative_1': [ButtonType.prox_rel.get_api_call, 3, 0],
                                    'Public_absolute_1': [ButtonType.prox_abs.get_api_call, 3, 0],
                                    'Public_relative_1': [ButtonType.prox_rel.get_api_call, 4, 0],
                                    'General_Public_absolute_1': [ButtonType.prox_abs.get_api_call, 4, 0],
                                    'General_Public_relative_1': [ButtonType.prox_rel.get_api_call, 5, 0],
                                    'Intimate_absolute_2': [ButtonType.prox_abs.get_api_call, 0, 1],
                                    'Intimate_relative_2': [ButtonType.prox_rel.get_api_call, 1, 1],
                                    'Personal_absolute_2': [ButtonType.prox_abs.get_api_call, 1, 1],
                                    'Personal_relative_2': [ButtonType.prox_rel.get_api_call, 2, 1],
                                    'Social_absolute_2': [ButtonType.prox_abs.get_api_call, 2, 1],
                                    'Social_relative_2': [ButtonType.prox_rel.get_api_call, 3, 1],
                                    'Public_absolute_2': [ButtonType.prox_abs.get_api_call, 3, 1],
                                    'Public_relative_2': [ButtonType.prox_rel.get_api_call, 4, 1],
                                    'General_Public_absolute_2': [ButtonType.prox_abs.get_api_call, 4, 1],
                                    'General_Public_relative_2': [ButtonType.prox_rel.get_api_call, 5, 1]
                                    }

        print(f'{api_prox_call_dict[fam_pattern][1]}, {api_prox_call_dict[fam_pattern][2]}')
        api_prox_call_dict[fam_pattern][0](api_prox_call_dict[fam_pattern][1],
                                              api_prox_call_dict[fam_pattern][2])
        print(f'finished vibrating for {fam_pattern}')

def next_press(btn):
    
    dist = dh.generate_distance()
    
    ButtonType.feet_abs.get_api_call(dist, 0) #feet_absolute1
    ButtonType.feet_abs.get_api_call(dist, 1) #feet_absolute2
    ButtonType.feet_rel.get_api_call(dist, 0) #feet_relative1
    ButtonType.feet_rel.get_api_call(dist, 1) #feet_relative2
    
    ButtonType.prox_abs.get_api_call(dist,0) #prox_absolute1
    ButtonType.prox_abs.get_api_call(dist,1) #prox_absolute2
    ButtonType.prox_rel.get_api_call(dist, 0) #prox_relative1
    ButtonType.prox_rel.get_api_call(dist, 1) #prox_relative2   

    
#Notebook is used for different tabs such as proximity,feet and familiarization
app.startNotebook("Notebook")

###############################################################################################################

#start of proximity tab
app.startNote("Proxemics")

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
app.addNamedButton("Restore","res1",restore,row=7,column=1,rowspan=0,colspan=0)

#This is just to align it properly
app.addLabel("                ",row=7,column=2,rowspan=0,colspan=0)
app.addNamedButton("Save","sav1",writeJson,row=7,column=3,rowspan=0,colspan=0)

app.addNamedButton("Next Pattern","nex1",next_press,row=7,column=4,rowspan=0,colspan=0)

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
app.addNamedButton("Restore","res2",restore,row=7,column=1,rowspan=0,colspan=0)

#This is just to align it properly
app.addLabel("               ",row=7,column=2,rowspan=0,colspan=0)
app.addNamedButton("Save","sav2",writeJson,row=7,column=3,rowspan=0,colspan=0)
app.addNamedButton("Next Pattern","nex2",next_press,row=7,column=4,rowspan=0,colspan=0)
app.stopNote()

###############################################################################################################

#start of Familiarization tab
app.startNote("Familiarization")

#All the buttons in Proximity tab- pr2,feet2 etc are the names. Proximity and Feet are the titles on button
#The radio buttons are grouped according to the proximity group and Feet group


app.addNamedButton("  Proxemics  ", "pr2", fam_press, row=0, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity", "Intimate", row=1, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity", "Personal", row=2,column=2,rowspan=0, colspan=0)
app.addRadioButton("proximity", "Social", row=3, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity", "Public", row=4, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity", "General_Public",row=5,column=2,rowspan=0, colspan=0)
app.setRadioButtonChangeFunction("proximity", change_fam_state)

app.addNamedButton("  Feet  ", "feet2", fam_press, row=0, column=4, rowspan=0, colspan=0)
app.addRadioButton("feet", "5", row=1, column=4, rowspan=0, colspan=0)
app.addRadioButton("feet", "10", row=2, column=4, rowspan=0, colspan=0)
app.addRadioButton("feet", "15", row=3, column=4, rowspan=0, colspan=0)
app.addRadioButton("feet", "20", row=4, column=4, rowspan=0, colspan=0)
app.addRadioButton("feet", "25", row=5, column=4, rowspan=0, colspan=0)
app.setRadioButtonChangeFunction("feet", change_fam_state)

app.addRadioButton("test_state", "absolute_1", row=1, column=6, rowspan=0, colspan=0)
app.addRadioButton("test_state", "relative_1", row=2, column=6, rowspan=0, colspan=0)
app.addRadioButton("test_state", "absolute_2", row=3, column=6, rowspan=0, colspan=0)
app.addRadioButton("test_state", "relative_2", row=4, column=6, rowspan=0, colspan=0)
app.setRadioButtonChangeFunction("test_state", change_fam_state)

#End of the 3 tabs
app.stopNotebook()

#End of the application
app.go()
