#!/usr/bin/python3
from appJar import gui
import datacollection as dc
from util.button_util import ButtonType
from typing import Dict
from tkinter.constants import CURRENT

# creating  class objects
dh = dc.DataHandler() # datahandler object

# This is the Entire dialog box with 1200 x 800 dimensions
app=gui("Grid Demo", useTtk=True)
app.setResizable(canResize=True)

# variables to keep track of familiarization radio buttons hit
fam_state_feet: str = '5'
fam_state_prox: str = 'Intimate'
fam_test_state: str = 'absolute_1'

app.setSticky("news")
app.setExpand("both")
app.setFont(20)

dist = 0
f_name = "default_name"
currentDistance = 0;
saveCtr = 0;

# Functions for the button
def press(btn):
    print(btn)


def repeat(btn):
    global currentDistance
    dh.repeatbtn()
    if btn is 'repeat_prox':
        mode = app.getListBox('prox_mode')
        print(f'\nrepeat testing, rand num is: {currentDistance}, select test: '
              f'{mode[0]}')
        test_dict: Dict = {
            "Absolute_1": [ButtonType.prox_abs.get_api_call, 0],
            # "Absolute_2": [ButtonType.prox_abs.get_api_call, 1],
            "Relative_1": [ButtonType.prox_rel.get_api_call, 0],
            # "Relative_2": [ButtonType.prox_rel.get_api_call, 1]
        }
        test_dict[mode[0]][0](dist,
                              test_dict[mode[0]][1])
        # TEMP
    elif btn is 'repeat_feet':
        mode = app.getListBox('feet_mode')
        print(f'\nrepeat testing, rand num is: {currentDistance}, select test: '
              f'{mode[0]}')
        test_dict: Dict = {
            "Absolute_1": [ButtonType.feet_abs.get_api_call, 0],
            # "Absolute_2": [ButtonType.feet_abs.get_api_call, 1],
            "Relative_1": [ButtonType.feet_rel.get_api_call, 0],
            # "Relative_2": [ButtonType.feet_rel.get_api_call, 1]
        }
        test_dict[mode[0]][0](currentDistance,
                              test_dict[mode[0]][1])
# TEMP
    print("finished repeat")

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



# def writeJson(btn):



    

# '''
# def chooseMode(btn):
#     item = app.getListBox("Mode")
#     print(item[0])
#     a = "Absolute"
#     b = "Relative"
#     if item[0] == a:
#         absolute()
#     elif item[0] == b:
#         relative()


# def chooseMode(btn):
#     item = app.getListBox("Mode1")
#     print(item[0])
#     a = "Absolute"
#     b = "Relative"
#     if item[0] == a:
#         absolute()
#     elif item[0] == b:
#         relative()

# '''


def writeJsonP():
    print(app.getRadioButton("proximity1"))


def writeJsonF():
    print(app.getRadioButton("feet1"))


def next_press(btn) -> None:
    print("next pressed")
    global dist, currentDistance, f_name, saveCtr
    
    saveCtr +=1
    dh.counterAdd()

    if saveCtr > 1:
    	get_user_response(btn)
    	dh.write_to_json()
    
    if(saveCtr == 31):
        f_name = app.textBox("Type file name", "Please type a file name here")
        print(f_name)
        dist = -1

        dh.save_results(f_name)
    elif(saveCtr == 16):
        print(btn)
        if btn is 'prox_next':
            crr = app.getListBox('prox_mode')
            app.removeListItem('prox_mode', crr)
        elif btn is 'feet_next':
            crr = app.getListBox('feet_mode')
            app.removeListItem('feet_mode', crr)
        dh.reset()

    proxft(btn)
    dist = dh.generate_distance()

    print("save: ",saveCtr)
    print("distance generated: ", dist)
    if dist == -1: #visited distances = 30 popup
        print("before pass")
        pass
        print("After pass")
    else:
        currentDistance = dist
        if btn is 'prox_next':
            mode = app.getListBox('prox_mode')
            print(f'testing prox_next, rand num is: {dist}, select test: '
                  f'{mode[0]}')
            test_dict: Dict = {
                "Absolute_1": [ButtonType.prox_abs.get_api_call, 0],
                # "Absolute_2": [ButtonType.prox_abs.get_api_call, 1],
                "Relative_1": [ButtonType.prox_rel.get_api_call, 0],
                # "Relative_2": [ButtonType.prox_rel.get_api_call, 1]
            }
            print("before api dist", dist)
            test_dict[mode[0]][0](dist,
                                  test_dict[mode[0]][1])

# TMEP
            print("After api")
            
            proxemicDistances = ["Intimate", "Personal", "Social", "Public", "General Public"]
            
            if dist == 0:
                app.setLabel("distance prox", "current distance: ")
            
            else:
                app.setLabel("distance prox", "current distance: " + proxemicDistances[dist-1])

            app.setLabel("pattern num", "Pattern: " + str(saveCtr))

            
        elif btn is 'feet_next':
            mode = app.getListBox('feet_mode')
            print(f'testing feet_next, rand num is: {dist}, select test: '
                  f'{mode[0]}')
            test_dict: Dict = {
                "Absolute_1": [ButtonType.feet_abs.get_api_call, 0],
                # "Absolute_2": [ButtonType.feet_abs.get_api_call, 1],
                "Relative_1": [ButtonType.feet_rel.get_api_call, 0],
                # "Relative_2": [ButtonType.feet_rel.get_api_call, 1]
            }
            test_dict[mode[0]][0](dist,
                                  test_dict[mode[0]][1])
# TMEP
            
            feetDistances = [5, 10, 15, 20, 25]

            if dist == 0:
                app.setLabel("distance feet", "current distance: ")
            
            else:
                app.setLabel("distance feet", "current distance: " + str(feetDistances[dist-1]))

            app.setLabel("pattern num2", "Pattern: " + str(saveCtr))

    print("finished next")

def get_user_response(btn):
    if btn is 'feet_next':
        dh.get_user_response(app.getRadioButton('feet1'), dist)
    elif btn is 'prox_next':
        dh.get_user_response(app.getRadioButton('proximity1'), dist)


def proxft(btn):
    if btn is 'feet_next':
        dh.get_prox_or_ft('feet')
        feetmode = app.getListBox('feet_mode')
        dh.get_abs_or_rel(feetmode)
    elif btn is 'prox_next':
        dh.get_prox_or_ft('proxemics')
        proxmode = app.getListBox('prox_mode')
        dh.get_abs_or_rel(proxmode)


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
        fam_pattern: str = fam_state_feet + f'_{fam_test_state}'
        print(f'vibrating for {fam_pattern}')
        api_feet_call_dict: Dict = {'5_absolute_1': [ButtonType.feet_abs.get_api_call, 1, 0,],
                                    '5_relative_1': [ButtonType.feet_rel.get_api_call, 1, 0,],
                                    '10_absolute_1':[ButtonType.feet_abs.get_api_call, 2, 0,],
                                    '10_relative_1': [ButtonType.feet_rel.get_api_call, 2, 0,],
                                    '15_absolute_1': [ButtonType.feet_abs.get_api_call, 3, 0,],
                                    '15_relative_1': [ButtonType.feet_rel.get_api_call, 3, 0,],
                                    '20_absolute_1': [ButtonType.feet_abs.get_api_call, 4, 0,],
                                    '20_relative_1': [ButtonType.feet_rel.get_api_call, 4, 0,],
                                    '25_absolute_1': [ButtonType.feet_abs.get_api_call, 5, 0,],
                                    '25_relative_1': [ButtonType.feet_rel.get_api_call, 5, 0,],
                                    # '5_absolute_2': [ButtonType.feet_abs.get_api_call, 1, 1,],
                                    # '5_relative_2': [ButtonType.feet_rel.get_api_call, 1, 1,],
                                    # '10_absolute_2': [ButtonType.feet_abs.get_api_call, 2, 1,],
                                    # '10_relative_2': [ButtonType.feet_rel.get_api_call, 2, 1,],
                                    # '15_absolute_2': [ButtonType.feet_abs.get_api_call, 3, 1,],
                                    # '15_relative_2': [ButtonType.feet_rel.get_api_call, 3, 1,],
                                    # '20_absolute_2': [ButtonType.feet_abs.get_api_call, 4, 1,],
                                    # '20_relative_2': [ButtonType.feet_rel.get_api_call, 4, 1,],
                                    # '25_absolute_2': [ButtonType.feet_abs.get_api_call, 5, 1,],
                                    # '25_relative_2': [ButtonType.feet_rel.get_api_call, 5, 1,]
                                    }

        print(f'{api_feet_call_dict[fam_pattern][1]}, {api_feet_call_dict[fam_pattern][2]}')
        api_feet_call_dict[fam_pattern][0](api_feet_call_dict[fam_pattern][1],
                                           api_feet_call_dict[fam_pattern][2])
# TEMP
        print(f'finished vibrating for {fam_state_feet}')

    if btn is 'pr2':
        print(f'vibrating for {fam_state_prox}')
        fam_pattern: str = fam_state_prox + f'_{fam_test_state}'
        api_prox_call_dict: Dict = {'Intimate_absolute_1': [ButtonType.prox_abs.get_api_call, 1, 0],
                                    'Intimate_relative_1': [ButtonType.prox_rel.get_api_call, 1, 0],
                                    'Personal_absolute_1': [ButtonType.prox_abs.get_api_call, 2, 0],
                                    'Personal_relative_1': [ButtonType.prox_rel.get_api_call, 2, 0],
                                    'Social_absolute_1': [ButtonType.prox_abs.get_api_call, 3, 0],
                                    'Social_relative_1': [ButtonType.prox_rel.get_api_call, 3, 0],
                                    'Public_absolute_1': [ButtonType.prox_abs.get_api_call, 4, 0],
                                    'Public_relative_1': [ButtonType.prox_rel.get_api_call, 4, 0],
                                    'General_Public_absolute_1': [ButtonType.prox_abs.get_api_call, 5, 0],
                                    'General_Public_relative_1': [ButtonType.prox_rel.get_api_call, 5, 0],
                                    # 'Intimate_absolute_2': [ButtonType.prox_abs.get_api_call, 1, 1],
                                    # 'Intimate_relative_2': [ButtonType.prox_rel.get_api_call, 1, 1],
                                    # 'Personal_absolute_2': [ButtonType.prox_abs.get_api_call, 2, 1],
                                    # 'Personal_relative_2': [ButtonType.prox_rel.get_api_call, 2, 1],
                                    # 'Social_absolute_2': [ButtonType.prox_abs.get_api_call, 3, 1],
                                    # 'Social_relative_2': [ButtonType.prox_rel.get_api_call, 3, 1],
                                    # 'Public_absolute_2': [ButtonType.prox_abs.get_api_call, 4, 1],
                                    # 'Public_relative_2': [ButtonType.prox_rel.get_api_call, 4, 1],
                                    # 'General_Public_absolute_2': [ButtonType.prox_abs.get_api_call, 5, 1],
                                    # 'General_Public_relative_2': [ButtonType.prox_rel.get_api_call, 5, 1]
                                    }

        print(f'{api_prox_call_dict[fam_pattern][1]}, {api_prox_call_dict[fam_pattern][2]}')
        api_prox_call_dict[fam_pattern][0](api_prox_call_dict[fam_pattern][1],
                                              api_prox_call_dict[fam_pattern][2])
        # TEMP
        print(f'finished vibrating for {fam_pattern}')
    
# Notebook is used for different tabs such as proximity,feet and familiarization
app.startNotebook("Notebook")

###############################################################################################################

#start of proximity tab
app.startNote("Proxemics")

# all the buttons in Proximity tab- ab1,rel1 etc are the names. Absolute, relative are the titles on button
app.addListBox("prox_mode", ["Absolute_1","Relative_1"], row=0,column=2, rowspan=0, colspan=0)
# app.addButton("Selected",chooseMode,row=0,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity1", "Intimate", row=2, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity1", "Personal", row=3, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity1", "Social", row=4, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity1", "Public", row=5, column=2, rowspan=0, colspan=0)
app.addRadioButton("proximity1", "General Public", row=6, column=2, rowspan=0, colspan=0)
# app.addLabelOptionBox("Mode", ["- Choose one -", "Absolute", "Relative"],row=0,column=2,rowspan=0,colspan=0)
# app.addNamedButton("Absolute","ab1",absolute,row=0,column=2,rowspan=0,colspan=0)
# app.addNamedButton("Relative","rel1",relative,row=1,column=2,rowspan=0,colspan=0)

app.addNamedButton("Repeat", "repeat_prox", repeat, row=7, column=0, rowspan=0, colspan=0)
app.addNamedButton("Restore", "res1", restore, row=7, column=1, rowspan=0, colspan=0)

# This is just to align it properly
app.addLabel("                ", row=7, column=2, rowspan=0, colspan=0)
# app.addNamedButton("Save","sav1",writeJson,row=7,column=3,rowspan=0,colspan=0)
app.addLabel("pattern num", "Pattern: ", row=6, column=4, rowspan=0, colspan=0)

app.addNamedButton("Next Pattern", "prox_next", next_press, row=7, column=4, rowspan=0, colspan=0)
#app.addLabel("distance title", text = "Distance: ", row = 6, column = 3, rowspan = 0, colspan = 0)
app.addLabel("distance prox", "current distance: ", row = 6, column = 3, rowspan = 0, colspan = 0)
# End of 1st tab
app.stopNote()

###############################################################################################################

# start of Feet tab
app.startNote("Feet")
# all the buttons in Proximity tab- ab1,rel1 etc are the names. Absolute, relative are the titles on button
app.addListBox("feet_mode", ["Absolute_1", "Relative_1"], row=0, column=2, rowspan=0, colspan=0)
# app.addButton("Selected ",chooseMode,row=0,column=2,rowspan=0,colspan=0)
app.addRadioButton("feet1", "5", row=2, column=2, rowspan=0, colspan=0)
app.addRadioButton("feet1", "10", row=3, column=2, rowspan=0, colspan=0)
app.addRadioButton("feet1", "15", row=4, column=2, rowspan=0, colspan=0)
app.addRadioButton("feet1", "20", row=5, column=2, rowspan=0, colspan=0)
app.addRadioButton("feet1", "25", row=6, column=2, rowspan=0, colspan=0)
# app.addLabelOptionBox("Mode", ["- Choose one -", "Absolute", "Relative"],row=0,column=2,rowspan=0,colspan=0)
# app.addNamedButton("Absolute","ab1",absolute,row=0,column=2,rowspan=0,colspan=0)
# app.addNamedButton("Relative","rel1",relative,row=1,column=2,rowspan=0,colspan=0)

app.addNamedButton("Repeat", "repeat_feet", repeat, row=7, column=0, rowspan=0, colspan=0)
app.addNamedButton("Restore", "res2", restore, row=7, column=1, rowspan=0, colspan=0)

# This is just to align it properly
app.addLabel("               ", row=7, column=2, rowspan=0, colspan=0)
# app.addNamedButton("Save","sav2",writeJson,row=7,column=3,rowspan=0,colspan=0)
app.addNamedButton("Next Pattern", "feet_next", next_press, row=7, column=4, rowspan=0, colspan=0)
app.addLabel("distance feet", "current distance: ", row = 6, column = 3, rowspan = 0, colspan = 0)
app.addLabel("pattern num2", "Pattern: ", row=6, column=4, rowspan=0, colspan=0)

app.stopNote()

###############################################################################################################

# start of Familiarization tab
app.startNote("Familiarization")

# All the buttons in Proximity tab- pr2,feet2 etc are the names. Proximity and Feet are the titles on button
# The radio buttons are grouped according to the proximity group and Feet group


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
# app.addRadioButton("test_state", "absolute_2", row=3, column=6, rowspan=0, colspan=0)
# app.addRadioButton("test_state", "relative_2", row=4, column=6, rowspan=0, colspan=0)
app.setRadioButtonChangeFunction("test_state", change_fam_state)


app.stopNote()

# End of the 3 tabs
app.stopNotebook()

# End of the application
app.go()
