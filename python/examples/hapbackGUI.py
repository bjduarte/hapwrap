#!/usr/bin/python3
from appJar import gui
import python.examples.datacollection as dc
from python.examples.util.button_util import ButtonType
from typing import Dict

 #creating  class objects
dh = dc.DataHandler() # datahandler object

# This is the Entire dialog box with 1200 x 800 dimensions
app = gui("Grid Demo", "1200x800", useTtk=True)

# variables to keep track of familiarization radio buttons hit
fam_state_feet: str = '5_abs'
fam_state_prox: str = 'Intimate_abs'
fam_test_state: str = 'abs'

app.setSticky("news")
app.setExpand("both")
app.setFont(20)


# Functions for the button
def press(btn):
    print(btn)


def repeat(btn):
    dh.repeatbtn()


def absolute(btn):
    dh.generate_distance()
    dh.get_abs_or_rel("absolute")
    dh.write_to_json()


def relative(btn):
    dh.generate_distance()
    dh.get_abs_or_rel("relative")
    dh.write_to_json()


def prox(btn):
    dh.get_prox_or_ft("proximate")


def feet(btn):
    dh.get_prox_or_ft("feet")


def write_json(btn):
    dh.write_to_json()


def change_fam_state(btn) -> None:
    global fam_state_feet, fam_state_prox, fam_test_state
    if btn is 'feet':
        fam_state_feet = app.getRadioButton('feet') + f'_{fam_test_state}'
        print(f'feet state is: {fam_state_feet}')
    elif btn is 'proximity':
        fam_state_prox = app.getRadioButton('proximity') + f'_{fam_test_state}'
        print(f'prox state is: {fam_state_prox}')
    elif btn is 'test_state':
        fam_test_state = app.getRadioButton('test_state')
        print(f'test state is: {fam_test_state}')


def fam_press(btn) -> None:
    global fam_state_feet, fam_state_prox
    if btn is 'feet2':
        print(f'vibrating for {fam_state_feet}')
        # api_feet_call_dict: Dict = {'5_absolute': ButtonType.feet_abs.get_api_call(1, 1),
        #                             '5_relative': ButtonType.feet_rel.get_api_call(1, 1),
        #                             '10_absolute': ButtonType.feet_abs.get_api_call(2, 1),
        #                             '10_relative': ButtonType.feet_rel.get_api_call(2, 1),
        #                             '15_absolute': ButtonType.feet_abs.get_api_call(3, 1),
        #                             '15_relative': ButtonType.feet_rel.get_api_call(3, 1),
        #                             '20_absolute': ButtonType.feet_abs.get_api_call(4, 1),
        #                             '20_relative': ButtonType.feet_rel.get_api_call(4, 1),
        #                             '25_absolute': ButtonType.feet_abs.get_api_call(5, 1),
        #                             '25_relative': ButtonType.feet_rel.get_api_call(5, 1)}
        #
        # api_feet_call_dict[fam_state_feet]

    if btn is 'pr2':
        print(f'vibrating for {fam_state_prox}')
        # api_prox_call_dict: Dict = {'Intimate_absolute': ButtonType.prox_abs.get_api_call(1, 1),
        #                             'Intimate_relative': ButtonType.prox_rel.get_api_call(1, 1),
        #                             'Personal_absolute': ButtonType.prox_abs.get_api_call(2, 1),
        #                             'Personal_relative': ButtonType.prox_rel.get_api_call(2, 1),
        #                             'Social_absolute': ButtonType.prox_abs.get_api_call(3, 1),
        #                             'Social_relative': ButtonType.prox_rel.get_api_call(3, 1),
        #                             'Public_absolute': ButtonType.prox_abs.get_api_call(4, 1),
        #                             'Public_relative': ButtonType.prox_rel.get_api_call(4, 1),
        #                             'General\ Public_absolute': ButtonType.prox_abs.get_api_call(5, 1),
        #                             'General\ Public_relative': ButtonType.prox_rel.get_api_call(5, 1)}
        #
        # api_prox_call_dict[fam_state_prox]


# Notebook is used for different tabs such as proximity,feet and familiarization
app.startNotebook("Notebook")

###############################################################################################################

# start of proximity tab
app.startNote("Proximity")

# all the buttons in Proximity tab- ab1,rel1 etc are the names. Absolute, relative are the titles on button
app.addNamedButton("Absolute","ab1",absolute,row=0,column=2,rowspan=0,colspan=0)
app.addNamedButton("Relative","rel1",relative,row=1,column=2,rowspan=0,colspan=0)
app.addNamedButton("Repeat","rep1",repeat,row=2,column=0,rowspan=0,colspan=0)
app.addNamedButton("Restore","res1",press,row=2,column=1,rowspan=0,colspan=0)

# This is just to align it properly
app.addLabel("                ",row=2,column=2,rowspan=0,colspan=0)
app.addNamedButton("Save","sav1",write_json,row=2,column=3,rowspan=0,colspan=0)
app.addNamedButton("Next Pattern","nex1",press,row=2,column=4,rowspan=0,colspan=0)

# End of 1st tab
app.stopNote()

###############################################################################################################

# start of Feet tab
app.startNote("Feet")
# all the buttons in Feet tab- ab2,rel2 etc are the names. Absolute, relative are the titles on button
app.addNamedButton("  Absolute  ", "ab2", absolute, row=0, column=2, rowspan=0, colspan=0)
app.addNamedButton("  Relative  ", "rel2", relative, row=1, column=2, rowspan=0, colspan=0)
app.addButton("Repeat", repeat, row=2, column=0, rowspan=0, colspan=0)
app.addButton("Restore", press, row=2, column=1, rowspan=0, colspan=0)
app.addLabel("               ", row=2, column=2, rowspan=0, colspan=0)
app.addButton("Save", write_json, row=2, column=3, rowspan=0, colspan=0)
app.addButton("Next Pattern", press, row=2, column=4, rowspan=0, colspan=0)
app.stopNote()

###############################################################################################################

# start of Familiarization tab
app.startNote("Familiarization")

# All the buttons in Proximity tab- pr2,feet2 etc are the names. Proximity and Feet are the titles on button
# The radio buttons are grouped according to the proximity group and Feet group

app.addNamedButton("  Proximity  ", "pr2", fam_press, row=0, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity", "Intimate", row=1, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity", "Personal", row=2,column=2,rowspan=0, colspan=0)
app.addRadioButton("proximity", "Social", row=3, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity", "Public", row=4, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity", "General Public",row=5,column=2,rowspan=0, colspan=0)
app.setRadioButtonChangeFunction("proximity", change_fam_state)

app.addNamedButton("  Feet  ", "feet2", fam_press, row=0, column=4, rowspan=0, colspan=0)
app.addRadioButton("feet", "5", row=1, column=4, rowspan=0, colspan=0)
app.addRadioButton("feet", "10", row=2, column=4, rowspan=0, colspan=0)
app.addRadioButton("feet", "15", row=3, column=4, rowspan=0, colspan=0)
app.addRadioButton("feet", "20", row=4, column=4, rowspan=0, colspan=0)
app.addRadioButton("feet", "25", row=5, column=4, rowspan=0, colspan=0)
app.setRadioButtonChangeFunction("feet", change_fam_state)

app.addRadioButton("test_state", "absolute", row=1, column=6, rowspan=0, colspan=0)
app.addRadioButton("test_state", "relative", row=2, column=6, rowspan=0, colspan=0)
app.setRadioButtonChangeFunction("test_state", change_fam_state)
app.stopNote()

# End of the 3 tabs
app.stopNotebook()

# End of the application
app.go()
