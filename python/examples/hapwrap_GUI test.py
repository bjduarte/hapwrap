#!/usr/bin/python3

# typing
from typing import List, Dict

# from kinter import *
from tkinter import ttk
from os.path import join as pjoin
import tkinter as tk

# from neopixel import *
import sys
import json
import random
import tkinter.messagebox as tk_message_box
import shutil
import os
import time
from os import path
# from complete_hapwrap_handler import *
from dynamic_pattern_list_builder import *

# LED strip configuration:
#LED_COUNT: int = 24  # Number of LED Labels.
#LED_PIN: int = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN: int = 10 # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
#LED_FREQ_H: int = 800000  # LED signal frequency in hertz (usually 800khz)
#LED_DMA: int = 10  # DMA channel to use for generating signal (try 10)
#LED_BRIGHTNESS: int = 255  # Set to 0 for darkest and 255 for brightest
#LED_INVERT: bool = False  # True to invert the signal (when using NPN transistor level shift)
#LED_CHANNEL: int = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

# pulse_on = Color(255, 255, 255)
# pulse_off = Color(0, 0, 0)

# hapwrap = Complete_hapwrap_handler()
heartbeat_pulse: int = 3
heartbeat_gap: float = 0.06  # gap between beats
heart_gap: float = 0.55  # duration beat is on
beat: int = 0

Root = tk.Tk()

RTitle = Root.title('HapWrap')
RWidth = Root.winfo_screenwidth()
RHeight = Root.winfo_screenheight()
Root.geometry('%dx%d' % (RWidth, RHeight))

# gives weight to the cells in the grid
rows: int = 0
while rows < 50:
    Root.rowconfigure(rows, weight=1)
    Root.columnconfigure(rows, weight=1)
    rows += 1

# Defines and places the notebook widget
eyes_on_screen = ttk.Notebook(Root)
eyes_on_screen.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

# Adds first tab of the notebook for static patterns
static_page = ttk.Frame(eyes_on_screen)
eyes_on_screen.add(static_page, text='Static Patterns')

# Adds second tab of the notebook for dynamic patterns
dynamic_page = ttk.Frame(eyes_on_screen)
eyes_on_screen.add(dynamic_page, text='Dynamic Patterns')

# Adds third tab of the notebook for familiarization
familiarization_page = ttk.Frame(eyes_on_screen)
eyes_on_screen.add(familiarization_page, text='Familiarization')

# create variable for button selection
static_pattern_num = tk.IntVar()
dynamic_pattern_num = tk.IntVar()
button_spacing = tk.IntVar()
distance_choice = tk.IntVar()
direction_choice = tk.IntVar()
elevation_choice = tk.IntVar()
user_dynamic_choice = tk.StringVar()
static_num_generated = tk.BooleanVar()
dynamic_num_generated = tk.BooleanVar()

# initialize variables
button_spacing: int = 0
static_pattern_num: int = 0
dynamic_pattern_num: int = 0
d_repeat_counter: int = 0
s_repeat_counter: int = 0
distance_choice.set(20)
direction_choice.set(20)
elevation_choice.set(20)

# button options
elevations: List = [('Head Height', 1), ('Chest Height', 2), ('Waist Height  ', 3)]
distances: List = [('10 feet', 1), ('15 feet', 2), ('20 feet', 3)]
directions: List = [('0', 1), ('45', 2), ('90', 3), ('135', 4), ('180', 5), ('225', 6), ('270', 7), ('315', 8)]

# lists of all the possible components that make up a pattern
elevation: List = [0, 1, 2]
distance: List = [0, 1, 2]
direction: List = [0, 1, 2, 3, 4, 5, 6, 7]

# Display button selection
dynamic_pattern = Dynamic_pattern_list_builder()  # initializes class to get dynamic patterns
static_incorrect_response: List = []
training_pattern: List = []
dynamic_incorrect_response: List = []
rand_num_list: List = []
static_counter: List = []
static_repeat_counter: List = []
dynamic_repeat_counter: List = []
dynamic_counter: List = []
visited_static_pattern: List = []
user_static_response: List = []
user_dynamic_response: List = []
d_rand_num_list: List = []  # list of random numbers for dynamic patterns
d_key_list: List = []  # list of keys
visited_dynamic_pattern: List = []  # list of visited dynamic patterns

# dictionary containning all static patterns
pattern_dict: Dict = {}
# iterate through each component to create a list of patterns
# elevation, distance, direction
pat = dynamic_pattern.pattern_builder()
current_static_pattern: List = []

# create list of keys, necessary for calling dynamic patterns
for i in pat:
    d_key_list.append(i)

num: int = 0
pattern_list: List = []
for i in elevation:
    for j in distance:
        for k in direction:
            pattern = [num, i, j, k]
            pattern_list.append(pattern)
            # pattern_dict['pattern list'] = pattern_list
            num += 1

# Patterns dictionary containing object positions
patterns: Dict = {
    'elevation': [1, 2, 3],
    'distance': [10, 15, 20],
    'direction': [[0, 45, 90, 135, 180, 225, 270, 315], [315, 270, 225, 180, 135, 90, 45, 0],
                  [0, 45, 90, 135, 180, 225, 270, 315]],
    'pin_out': [[0, 1, 2, 3, 4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8], [16, 17, 18, 19, 20, 21, 22, 23]]}


def static_heartbeat():
    global pix, beat

    pix = patterns.get('pin_out')[training_pattern[0]][training_pattern[2]]
    pix_pointer = patterns.get('pin_out')[1][training_pattern[2]]
    print('pix = ' + str(pix))
    print('pix_pointer = ' + str(pix_pointer))

    # Heart beat code
    # select heart gap for distance
    if training_pattern[1] == 0:
        beat = 0.25
    elif training_pattern[1] == 1:
        beat = 0.50
    elif training_pattern[1] == 2:
        beat = 1.00


# Pointer beat
# if ((training_pattern[1] == 2) or (training_pattern[1] == 0) or (training_pattern[1] == 1)):
#     print (training_pattern[1])
#     strip.setPixelColor(pix_pointer,pulse_on)
#     print ('On')
#     strip.show()
#     print(beat)
#     time.sleep(0.99)

#     strip.setPixelColor(pix_pointer,pulse_off)
#     print ('Off')
#     strip.show()
#     print(beat)
#     time.sleep(heartbeat_gap)

#     print('Beginning Heartbeat')
#     for x in range(heartbeat_pulse):
#         strip.setPixelColor(pix,pulse_on)
#         print ('On')
#         strip.show()
#         print(beat)
#         time.sleep(heart_gap)

#         strip.setPixelColor(pix,pulse_off)
#         print ('Off')
#         strip.show()
#         print(beat)
#         time.sleep(heartbeat_gap)

#         strip.setPixelColor(pix,pulse_on)
#         print ('On')
#         strip.show()
#         print(beat)
#         time.sleep(heart_gap)

#         strip.setPixelColor(pix,pulse_off)
#         print ('Off')
#         strip.show()
#         print(beat)
#         time.sleep(beat)


def familiarization_tab():
    global patterns, static_pattern_num, training_pattern, button_spacing

    try:
        training_pattern = [elevations[elevation_choice.get() - 1][1] - 1,
                            distances[distance_choice.get() - 1][1] - 1,
                            directions[direction_choice.get() - 1][1] - 1]
    except IndexError:
        try:
            training_pattern = [elevations[elevation_choice.get() - 1][1] - 1,
                                distances[distance_choice.get() - 1][1] - 1,
                                0]
        except IndexError:
            try:
                training_pattern = [0, distances[distance_choice.get() - 1][1] - 1,
                                    directions[direction_choice.get() - 1][1] - 1]
            except IndexError:
                try:
                    training_pattern = [elevations[elevation_choice.get() - 1][1] - 1, 0,
                                        directions[direction_choice.get() - 1][1] - 1]
                except IndexError:
                    try:
                        training_pattern = [elevations[elevation_choice.get() - 1][1] - 1, 0, 0]
                    except IndexError:
                        try:
                            training_pattern = [0, distances[distance_choice.get() - 1][1] - 1, 0]
                        except IndexError:
                            try:
                                training_pattern = [0, 0, directions[direction_choice.get() - 1][1] - 1]
                            except IndexError:
                                training_pattern = [0, 0, 0]

    button_spacing = 0
    print(training_pattern)

    # heartbeat code was here!

    # set the elevation, direction, and distance radiobuttons outside their range
    # so it appears cleared each time new pattern generated
    elevation_choice.set(20)
    direction_choice.set(20)
    distance_choice.set(20)


# function for the next button on the static page
def next_static_click():
    # r_num has to initialized globally if a reference is going to be made==============NOTE===============
    global patterns, r_num, s_repeat_counter, static_pattern_num, button_spacing, static_num_generated

    repeat_message = ttk.Label(static_page, text='                                                    ')
    repeat_message.place(x=RWidth - 6 * RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)
    static_pattern_num = static_pattern_num + 1
    pattern_dict['static counter'] = static_counter
    static_counter.append(static_pattern_num)
    static_num_generated = False

    # create elevation buttons
    static_next_button.configure(state=tk.DISABLED)
    button_spacing = 0

    # Each time next button is clicked status message is changed back to unsaved
    status_message = ttk.Label(static_page, text='Status: UNSAVED')
    status_message.place(x=RWidth - 2 * RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)


# heartbeat handler for static tab
def static_heart_beat_handler():
    global pix, beat, distances, r_num, static_num_generated, button_spacing, elevation_button, \
        clear_elevation_button, clear_distance_button, distance_button, direct_button, static_incorrect_response, \
        clear_direction_button, s_repeat_counter, current_static_pattern
    pix = patterns.get('pin_out')[current_static_pattern[1]][current_static_pattern[3]]
    pix_pointer = patterns.get('pin_out')[1][current_static_pattern[3]]
    print(current_static_pattern)
    print('pix = ' + str(pix))
    print('pix_pointer = ' + str(pix_pointer))
    beat = 0
    # Heart beat code
    if distances[current_static_pattern[2]][0] == '10 feet':
        beat = 0.25
    elif distances[current_static_pattern[2]][0] == '15 feet':
        beat = 0.50
    elif distances[current_static_pattern[2]][0] == '20 feet':
        beat = 1.00
    # # Heartbeat pattern for 10 through 20 feet
    # if ((distances[current_static_pattern[2]][0] == '20 feet') or
    #         (distances[current_static_pattern[2]][0] == '10 feet') or
    #         (distances[current_static_pattern[2]][0] == '15 feet')):
    #     strip.setPixelColor(pix_pointer,pulse_on)
    #     print ('On')
    #     strip.show()
    #     print(beat)
    #     time.sleep(0.99)
    #     strip.setPixelColor(pix_pointer,pulse_off)
    #     print ('Off')
    #     strip.show()
    #     print(beat)
    #     time.sleep(heartbeat_gap)
    #     print('Beginning Heartbeat')
    #     for x in range(heartbeat_pulse):
    #         strip.setPixelColor(pix,pulse_on)
    #         print ('On')
    #         strip.show()
    #         print(beat)
    #         time.sleep(heart_gap)
    #         strip.setPixelColor(pix,pulse_off)
    #         print ('Off')
    #         strip.show()
    #         print(beat)
    #         time.sleep(heartbeat_gap)
    #         strip.setPixelColor(pix,pulse_on)
    #         print ('On')
    #         strip.show()
    #         print(beat)
    #         time.sleep(heart_gap)
    #         strip.setPixelColor(pix,pulse_off)
    #         print ('Off')
    #         strip.show()
    #         print(beat)
    #         time.sleep(beat)

    # generates a random number and calls a pattern
    # tries to check for duplicate random numbers
    if static_pattern_num <= 31 & static_pattern_num > 0:
        # while static_num_generated == FALSE
        while not static_num_generated:
            r_num = random.randint(0, 71)
            while r_num not in rand_num_list:
                rand_num_list.append(r_num)
                current_static_pattern = pattern_list[r_num]
                static_num_generated = True

        pix = patterns.get('pin_out')[current_static_pattern[1]][current_static_pattern[3]]
        pix_pointer = patterns.get('pin_out')[1][current_static_pattern[3]]
        print(current_static_pattern)
        print('pix = ' + str(pix))
        print('pix_pointer = ' + str(pix_pointer))
        beat = 0

        # Heart beat code
        if distances[current_static_pattern[2]][0] == '10 feet':
            beat = 0.25
        elif distances[current_static_pattern[2]][0] == '15 feet':
            beat = 0.50
        elif distances[current_static_pattern[2]][0] == '20 feet':
            beat = 1.00

        # # Heartbeat pattern for 10 through 20 feet
        # if ((distances[current_static_pattern[2]][0] == '20 feet') or
        #         (distances[current_static_pattern[2]][0] == '10 feet') or
        #         (distances[current_static_pattern[2]][0] == '15 feet')):
        #     strip.setPixelColor(pix_pointer,pulse_on)
        #     print ('On')
        #     strip.show()
        #     print(beat)
        #     time.sleep(0.99)

        #     strip.setPixelColor(pix_pointer,pulse_off)
        #     print ('Off')
        #     strip.show()
        #     print(beat)
        #     time.sleep(heartbeat_gap)
        #     print('Beginning Heartbeat')

        #     for x in range(heartbeat_pulse):
        #         strip.setPixelColor(pix,pulse_on)
        #         print ('On')
        #         strip.show()
        #         print(beat)
        #         time.sleep(heart_gap)

        #         strip.setPixelColor(pix,pulse_off)
        #         print ('Off')
        #         strip.show()
        #         print(beat)
        #         time.sleep(heartbeat_gap)

        #         strip.setPixelColor(pix,pulse_on)
        #         print ('On')
        #         strip.show()
        #         print(beat)
        #         time.sleep(heart_gap)

        #         strip.setPixelColor(pix,pulse_off)
        #         print ('Off')
        #         strip.show()
        #         print(beat)
        #         time.sleep(beat)

        for text_, elevation_ in elevations:
            elevation_button = ttk.Radiobutton(static_page, text=text_, variable=elevation_choice, value=elevation_)
            button_spacing = button_spacing + 30
            elevation_button.place(x=RWidth / 4, y=(RHeight / 4) + 5 + button_spacing, anchor=tk.CENTER)
            # create clearElevation button
        clear_elevation_button = ttk.Button(static_page, text='Clear', command=clear_elevation_selection)
        clear_elevation_button.place(x=RWidth / 4, y=(RHeight / 4) + 5 + 120, anchor=tk.CENTER)

        # create distance buttons
        button_spacing = 0
        for text_, distance_ in distances:
            distance_button = ttk.Radiobutton(static_page, text=text_, variable=distance_choice, value=distance_)
            button_spacing = button_spacing + 30
            distance_button.place(x=2 * RWidth / 4, y=(RHeight / 4) + 5 + button_spacing, anchor=tk.CENTER)
            # create clearDistance button
        clear_distance_button = ttk.Button(static_page, text='Clear', command=clear_distance_selection)
        clear_distance_button.place(x=2 * RWidth / 4, y=(RHeight / 4) + 5 + 150, anchor=tk.CENTER)

        # create direction buttons
        button_spacing = 0
        for text_, direction_ in directions:
            direct_button = ttk.Radiobutton(static_page, text=text_, variable=direction_choice, value=direction_)
            button_spacing = button_spacing + 30
            direct_button.place(x=3 * RWidth / 4, y=(RHeight / 4) + 5 + button_spacing, anchor=tk.CENTER)
            # create clearDirection button
        clear_direction_button = ttk.Button(static_page, text='Clear', command=clear_direction_selection)
        clear_direction_button.place(x=3 * RWidth / 4, y=(RHeight / 4) + 5 + 270, anchor=tk.CENTER)

        # create pattern text to display current pattern
        # dynamic_next_button.configure(state=tk.DISABLED)
        patter_message = ttk.Label(static_page, text='Pattern ' + str(static_pattern_num))
        patter_message.place(x=RWidth - RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)

        current_static_pattern_message = ttk.Label(static_page, text='Current Static Pattern:\nElevation = ' + str(
            elevations[current_static_pattern[1]][0]) + '\nDistance = ' + str(
            distances[current_static_pattern[2]][0]) + '\nDirection = ' + str(directions[current_static_pattern[3]][0]))
        current_static_pattern_message.place(x=19 * RWidth / 40, y=RHeight - 200, anchor=tk.CENTER)

    if static_pattern_num <= 30 & static_pattern_num > 1:
        # keep track of participants answers
        # radio button presses will be read in and saved
        try:
            static_incorrect_response = [elevations[elevation_choice.get() - 1][0],
                                         distances[distance_choice.get() - 1][0],
                                         directions[direction_choice.get() - 1][0]]
        except IndexError:
            try:
                static_incorrect_response = [elevations[elevation_choice.get() - 1][0],
                                             distances[distance_choice.get() - 1][0], 0]
            except IndexError:
                try:
                    static_incorrect_response = [0, distances[distance_choice.get() - 1][0],
                                                 directions[direction_choice.get() - 1][0]]
                except IndexError:
                    try:
                        static_incorrect_response = [elevations[elevation_choice.get() - 1][0], 0,
                                                     directions[direction_choice.get() - 1][0]]
                    except IndexError:
                        try:
                            static_incorrect_response = [elevations[elevation_choice.get() - 1][0], 0, 0]
                        except IndexError:
                            try:
                                static_incorrect_response = [0, distances[distance_choice.get() - 1][0], 0]
                            except IndexError:
                                try:
                                    static_incorrect_response = [0, 0, directions[direction_choice.get() - 1][0]]
                                except IndexError:
                                    static_incorrect_response = [0, 0, 0]
        user_static_response.append(static_incorrect_response)
        print('This is the incorrect response: ' + str(user_static_response))
        print('This is the user static response ' + str(user_static_response))

        visited_static_pattern.append(current_static_pattern)
        pattern_dict['visited static patterns'] = visited_static_pattern
        static_repeat_counter.append(s_repeat_counter)
        pattern_dict['Static Repeat Counter'] = static_repeat_counter
        s_repeat_counter = 0
        pattern_dict['user static response'] = user_static_response

        # write pattern_dict to json file called userData.json
        f = open('userData.json', 'w')
        f.write(json.dumps(pattern_dict, sort_keys=True, indent=1))
        f.close()
        print('static_pattern_num' + str(static_pattern_num))

        if static_pattern_num == 30:
            file = open('userData.json', 'r')
            fin = json.load(file)
            file.close()

            static_results = fin.get('user static response')
            # Debugging
            print(static_results)
            num_static_correct = 0
            for row in range(len(static_results)):
                if static_results[row][0] == 0:
                    num_static_correct = (num_static_correct + 1)
                if static_results[row][1] == 0:
                    num_static_correct = (num_static_correct + 1)
                if static_results[row][2] == 0:
                    num_static_correct = (num_static_correct + 1)

            static_score = num_static_correct / float(87) * 100

            print('Static Score = ' + str(static_score) + '%')
            # pop-up window displays percentage correct for static training
            tk_message_box.showinfo('Score', 'Static Score: ' + str(static_score) + '%')

            pattern_dict['Static Score'] = str(static_score) + '%'

            # write pattern_dict to json file called userData.json
            f = open('userData.json', 'w')
            f.write(json.dumps(pattern_dict, sort_keys=True, indent=1))
            f.close()

            patter_message = ttk.Label(static_page, text='Done')
            patter_message.place(x=RWidth - RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)
            current_static_pattern_message = ttk.Label(static_page, text='All 30 patterns have been done')
            current_static_pattern_message.place(x=19 * RWidth / 40, y=RHeight - 200, anchor=tk.CENTER)

            # set the elevation, direction, and distance radiobuttons outside their range
            # so it appears cleared each time new pattern generated
    elevation_choice.set(20)
    direction_choice.set(20)
    distance_choice.set(20)


# function for saving response when next is clicked
'''
def click_next():
    global current_dynamic_pattern
    global dynamic_pattern_num
    global d_repeat_counter
    global visited_static_pattern
    global static_counter
    global static_repeat_counter
    global user_static_response
    global pix
    global beat
    global file_name
    global dynamic_incorrect_response
    global d_key_list

    click_next()

'''


def click_next():
    global dynamic_incorrect_response
    dynamic_incorrect_response = user_dynamic_choice.get()
    user_dynamic_response.append(dynamic_incorrect_response)
    pattern_dict['user dynamic response'] = user_dynamic_response
    pattern_dict['dynamic counter'] = dynamic_counter
    # write pattern_dict to json file called userData.json
    f = open('userData.json', 'w')
    f.write(json.dumps(pattern_dict, sort_keys=True, indent=1))
    f.close()


# function for the next button on the dynamic page
'''
def next_dynamic_click(): 

    global current_dynamic_pattern
    global dynamic_pattern_num
    global d_repeat_counter
    global visited_static_pattern
    global static_counter
    global static_repeat_counter
    global user_static_response
    global pix
    global beat
    global file_name
    global dynamic_incorrect_response
    global d_key_list

    next_dynamic_click(d_key_list, static_counter, static_repeat_counter, user_static_response, visited_static_pattern)
'''


def next_dynamic_click():
    global dynamic_pattern_num, d_repeat_counter, current_dynamic_pattern, pix, beat, file_name, dynamic_user_response, \
        dynamic_num_generated
    print('This is the user static response ' + str(user_static_response))
    dynamic_next_button.configure(state=tk.DISABLED)
    dynamic_num_generated = False
    dynamic_pattern_num = dynamic_pattern_num + 1
    dynamic_counter.append(dynamic_pattern_num)
    repeat_message = ttk.Label(dynamic_page, text='                                                    ')
    repeat_message.place(x=RWidth - 6 * RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)
    information_message = ttk.Label(dynamic_page, text='Enter User Response:')
    information_message.place(x=(RWidth - 50) / 2, y=RHeight / 3 - 50, anchor=tk.CENTER)
    dynamic_user_response = ttk.Entry(dynamic_page, width=30, textvariable=user_dynamic_choice)
    dynamic_user_response.place(x=(RWidth - 50) / 2, y=RHeight / 3, anchor=tk.CENTER)

    dynamic_heartbeat_handler(dynamic_pattern_num, dynamic_user_response)


def dynamic_heartbeat_handler(dynamic_pattern_num, dynamic_user_response):
    global d_repeat_counter, current_dynamic_pattern, pix, beat, file_name, r_num, elevation, distance, direction, \
        dynamic_num_generated
    if dynamic_pattern_num > 1 and dynamic_pattern_num < 18:
        pattern_dict['visited static patterns'] = visited_static_pattern
        pattern_dict['static counter'] = static_counter
        pattern_dict['Static Repeat Counter'] = static_repeat_counter
        pattern_dict['user static response'] = user_static_response

        dynamic_repeat_counter.append(d_repeat_counter)
        pattern_dict['Dynamic Repeat Counter'] = dynamic_repeat_counter
        d_repeat_counter = 0
        # save user response when next is clicked
        click_next()
        '''
        dynamic_incorrect_response = user_dynamic_choice.get()
        user_dynamic_response.append(dynamic_incorrect_response)
        pattern_dict['user dynamic response'] = user_dynamic_response
        pattern_dict['dynamic counter'] = dynamic_counter
        # write pattern_dict to json file called userData.json
        f = open('userData.json','w')
        f.write(json.dumps(pattern_dict, sort_keys=True, indent=1))
        f.close()
        '''
    # clear the entry field
    dynamic_user_response.delete(0, tk.END)
    if dynamic_pattern_num < 18:
        # while not dynamic_num_generated == FALSE
        while not dynamic_num_generated:
            r_num = random.randint(0, 16)
            pointer_done = False
            print(r_num)
            print(d_key_list)
            while r_num not in d_rand_num_list:
                d_rand_num_list.append(r_num)
                current_dynamic_pattern = d_key_list[r_num]
                visited_dynamic_pattern.append(current_dynamic_pattern)
                pattern_dict['visited dynamic patterns'] = visited_dynamic_pattern
                dynamic_num_generated = True

        for currentBeat in pat.get(current_dynamic_pattern):
            print(pat.get(current_dynamic_pattern))
            print(currentBeat)
            elevation = currentBeat[0]
            distance = currentBeat[1]
            direction = currentBeat[2]
            print('elevation: ' + str(elevation) + ' ' + 'distance: ' + str(distance) + ' ' + 'direction: ' + str(
                direction))
            print(current_dynamic_pattern)
            pix = patterns.get('pin_out')[elevation][direction]
            print('pix = ' + str(pix))
            beat = 0

            if distance == 0:
                # print ('distance is 0')
                beat = 0.25
            elif distance == 1:
                # print ('distance is 1')
                beat = 0.50
            elif distance == 2:
                # print ('distance is 2')
                beat = 1.00

            # pix_pointer Pattern
            # if (pointer_done == False):
            #     pix_pointer = patterns.get('pin_out')[1][direction]
            #     print('pix_pointer = ' + str(pix_pointer))
            #     strip.setPixelColor(pix_pointer,pulse_on)
            #     print ('On')
            #     strip.show()
            #     print(beat)
            #     time.sleep(0.99)

            #     strip.setPixelColor(pix_pointer,pulse_off)
            #     print ('Off')
            #     strip.show()
            #     print(beat)
            #     time.sleep(heartbeat_gap)
            #     print('Beginning Heartbeat')
            #     pointer_done = True

            # # Heartbeat pattern for 10 through 20 feet
            # if ((distance == 2) or (distance == 1) or (distance == 0)):
            #     for x in range(heartbeat_pulse):
            #         strip.setPixelColor(pix,pulse_on)
            #         print ('On')
            #         strip.show()
            #         print(beat)
            #         time.sleep(heart_gap)

            #         strip.setPixelColor(pix,pulse_off)
            #         print ('Off')
            #         strip.show()
            #         print(beat)
            #         time.sleep(heartbeat_gap)

            #         strip.setPixelColor(pix,pulse_on)
            #         print ('On')
            #         strip.show()
            #         print(beat)
            #         time.sleep(heart_gap)

            #         strip.setPixelColor(pix,pulse_off)
            #         print ('Off')
            #         strip.show()
            #         print(beat)
            #         time.sleep(beat)

        # create dynamic status text
        status_message = ttk.Label(dynamic_page, text='Status: UNSAVED')
        status_message.place(x=RWidth - 2 * RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)
        patter_message = ttk.Label(dynamic_page, text='Pattern ' + str(dynamic_pattern_num))
        patter_message.place(x=RWidth - RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)
        current_static_pattern_message = ttk.Label(dynamic_page,
                                                   text=f'''Current Dynamic Pattern:\n {current_dynamic_pattern}''')
        current_static_pattern_message.place(x=19 * RWidth / 40, y=RHeight - 200, anchor=tk.CENTER)
    if dynamic_pattern_num >= 18:

        pattern_dict['visited static patterns'] = visited_static_pattern
        pattern_dict['visited dynamic patterns'] = visited_dynamic_pattern
        pattern_dict['static counter'] = static_counter
        pattern_dict['Static Repeat Counter'] = static_repeat_counter
        pattern_dict['user static response'] = user_static_response
        # save user response when next is clicked
        dynamic_repeat_counter.append(d_repeat_counter)

        pattern_dict['Dynamic Repeat Counter'] = dynamic_repeat_counter

        click_next()
        '''
        dynamic_incorrect_response = user_dynamic_choice.get()
        user_dynamic_response.append(dynamic_incorrect_response)
        pattern_dict['user dynamic response'] = user_dynamic_response
        pattern_dict['dynamic counter'] = dynamic_counter
        # write pattern_dict to json file called userData.json
        f = open('userData.json','w')
        f.write(json.dumps(pattern_dict, sort_keys=True, indent=1))
        f.close()
        '''

        file = open('userData.json', 'r')
        fin = json.load(file)
        file.close()

        dynamic_results = fin.get('user dynamic response')
        num_dynamic_correct = 0
        i = 0
        while i < len(dynamic_results):
            if len(dynamic_results[i]) == 0:
                num_dynamic_correct = (num_dynamic_correct + 1)
            i += 1
        dynamic_score = num_dynamic_correct / float(17) * 100

        print('Dynamic Score: ' + str(dynamic_score) + '%')
        # pop-up window displays percentage correct for dynamic training
        tk_message_box.showinfo('Score', 'Dynamic Score: ' + str(dynamic_score) + '%')
        pattern_dict['Dynamic Score'] = str(dynamic_score) + '%'

        # write pattern_dict to json file called userData.json
        f = open('userData.json', 'w')
        f.write(json.dumps(pattern_dict, sort_keys=True, indent=1))
        f.close()
        file_name = ttk.Entry(dynamic_page, width=30)
        file_name.place(x=(RWidth - 50) / 2, y=RHeight / 6, anchor=tk.CENTER)
        file_info = ttk.Label(dynamic_page, text='Enter a file name:')
        file_info.place(x=(RWidth - 50) / 2, y=RHeight / 6 - 45, anchor=tk.CENTER)
        file_button = ttk.Button(dynamic_page, text='Save file', command=file_button_click)
        file_button.place(x=(RWidth - 50) / 2 + 200, y=RHeight / 6, anchor=tk.CENTER)
        dynamicSaveButton.configure(state=tk.DISABLED)
        dynamic_next_button.configure(state=tk.DISABLED)
        patter_message = ttk.Label(dynamic_page, text='Done          ')
        patter_message.place(x=RWidth - RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)
        current_static_pattern_message = ttk.Label(dynamic_page, text='All 23 patterns have been done\n\n')
        current_static_pattern_message.place(x=19 * RWidth / 40, y=RHeight - 200, anchor=tk.CENTER)


# function for saving the study results after the user inputs a file name
def file_button_click():
    file_choice = file_name.get()

    # reads in the json file to be parsed
    file = open('userData.json', 'r')
    fin = json.load(file)
    file.close()
    # writes dynamic data to a text file formatted together
    static = zip(fin.get('static counter'), fin.get('visited static patterns'), fin.get('user static response'),
                 fin.get('Static Repeat Counter'))
    dynamic = zip(fin.get('dynamic counter'), fin.get('visited dynamic patterns'), fin.get('user dynamic response'),
                  fin.get('Dynamic Repeat Counter'))
    # writes the static data to a text file formatted together

    # f = open('output.txt', 'w+')
    cwd = os.getcwd()
    path_to_file = pjoin(cwd, 'completedStudies', file_choice)
    f = open(path_to_file, 'w+')

    f.write('Count|Static Pattern|User Response|Times Repeated\n')
    for i in static:
        f.write(str(i) + '\n')

    f.write('Static Score:\n')
    # f.write(str(fin.get('Static Score')))

    f.write('\nCount|Dynamic Pattern|User Response|Times Repeated\n')
    for j in dynamic:
        f.write(str(j) + '\n')

    f.write('Dynamic Score:\n')
    f.write(str(fin.get('Dynamic Score')))

    f.close()

    # save file to folder called completedStudies
    print('saved to ' + file_choice + '.txt')
    # shutil.move('Eyes_on/python/examples/' + file_choice + '.txt',
    #             'Eyes_On/python/examples/completedStudies/'  + file_choice + '.txt')
    tk_message_box.showinfo('File Status', 'Data stored to ' + file_choice + '.txt')


# function for the save button on the dynamic page
def dynamic_save_click():
    global dynamic_user_response
    if dynamic_pattern_num < 18:
        dynamic_next_button.configure(state=tk.NORMAL)

    status_message = ttk.Label(dynamic_page, text='  Status: SAVED  ')
    lsum = ttk.Label(master, text='Your input is:')
    lsum.grid(row=30, column=30, sticky=W, pady=5)
    lsum['text'] = 'Your input is: ' + dynamic_user_response


# function for the save button on the static page
def static_save_click():
    global static_incorrect_response

    if static_pattern_num < 31:
        static_next_button.configure(state=tk.NORMAL)
    else:
        staticSaveButton.configure(state=tk.DISABLED)

    status_message = ttk.Label(static_page, text='  Status: SAVED  ')
    status_message.place(x=RWidth - 2 * RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)


'''
#function for the restore button on the static page
def restoreStaticClick():
    global static_pattern_num
    static_next_button.configure(state=tk.NORMAL)
    staticSaveButton.configure(state=tk.NORMAL)
    staticRepeatButton.configure(state=tk.NORMAL)

    try:
        f = open('userData.json', 'r')
        fin = json.load(f)
        f.close()
        #type(fin)
        for i in fin['visited static patterns']:
            visited_static_pattern.append(i)
            print ('worked1')
        for i in fin['user static response']:
            user_static_response.append(i)
            print ('worked2')
        for i in fin['static counter']:
            static_counter.append(i)
            print ('worked3')
        for i in fin['Static Repeat Counter']:
            static_repeat_counter.append(i)
            print ('worked4')
        static_pattern_num = fin['static counter'][-1] - 1
        print ('worked5')

    except:
            print('nothing to restore')
            tk_message_box.showinfo('Restore', 'Nothing to restore')

#function for the restore button on the dynamic page
def restoreDynamicClick():
    restore_click()
'''


def restore_click():
    global dynamic_pattern_num
    dynamic_next_button.configure(state=tk.NORMAL)
    dynamicSaveButton.configure(state=tk.NORMAL)
    dynamicRepeatButton.configure(state=tk.NORMAL)
    try:
        f = open('userData.json', 'r')
        fin = json.load(f)
        f.close()

        for i_ in fin['visited static patterns']:
            visited_static_pattern.append(i_)
            print('dworked7')
        for i_ in fin['user static response']:
            user_static_response.append(i_)
            print('dworked8')
        for i_ in fin['static counter']:
            static_counter.append(i_)
            print('dworked9')
        for i_ in fin['visited dynamic patterns']:
            visited_dynamic_pattern.append(i_)
            print('dworked1')
        for i_ in fin['user dynamic response']:
            user_dynamic_response.append(i_)
            print('dworked2')
        for i_ in fin['dynamic counter']:
            dynamic_counter.append(i_)
            print('dworked3')
        for i_ in fin['Static Repeat Counter']:
            static_repeat_counter.append(i_)
            print('dworked4')
        for i_ in fin['Dynamic Repeat Counter']:
            dynamic_repeat_counter.append(i_)
            print('dworked5')
        dynamic_pattern_num = fin['dynamic counter'][-1] - 1
        print('dworked6')

    except:
        print('nothing to restore')
        tk_message_box.showinfo('Restore', 'Nothing to restore')


# function for the repeat button on the Dynamic Page
def repeat_dynamic_click():
    global d_repeat_counter, elevation, distance, direction, pix, beat
    d_repeat_counter = d_repeat_counter + 1
    pointer_done = False
    for currentBeat in pat.get(current_dynamic_pattern):
        print(pat.get(current_dynamic_pattern))
        print(currentBeat)
        elevation = currentBeat[0]
        distance = currentBeat[1]
        direction = currentBeat[2]
        print(
            'elevation: ' + str(elevation) + ' ' + 'distance: ' + str(distance) + ' ' + 'direction: ' + str(direction))
        print(current_dynamic_pattern)
        pix = patterns.get('pin_out')[elevation][direction]
        print('pix = ' + str(pix))
        beat = 0

        if distance == 0:
            print('distance is 0')
            beat = 0.25
        elif distance == 1:
            print('distance is 1')
            beat = 0.50
        elif distance == 2:
            print('distance is 2')
            beat = 1.00
        # pix_pointer Pattern
        # if (pointer_done == False):
        #     pix_pointer = patterns.get('pin_out')[1][direction]
        #     print('pix_pointer = ' + str(pix_pointer))
        #     strip.setPixelColor(pix_pointer,pulse_on)
        #     print ('On')
        #     strip.show()
        #     print(beat)
        #     time.sleep(0.99)

        #     strip.setPixelColor(pix_pointer,pulse_off)
        #     print ('Off')
        #     strip.show()
        #     print(beat)
        #     time.sleep(heartbeat_gap)
        #     print('Beginning Heartbeat')
        #     pointer_done = True

        # # # Heartbeat pattern for 10 through 20 feet
        # if ((distance == 2) or (distance == 1) or (distance == 0)):
        #     for x in range(heartbeat_pulse):
        #         strip.setPixelColor(pix,pulse_on)
        #         print ('On')
        #         strip.show()
        #         print(beat)
        #         time.sleep(heartbeat_gap)

        #         strip.setPixelColor(pix,pulse_off)
        #         print ('Off')
        #         strip.show()
        #         print(beat)
        #         time.sleep(heartbeat_gap)

        #         strip.setPixelColor(pix,pulse_on)
        #         print ('On')
        #         strip.show()
        #         print(beat)
        #         time.sleep(heartbeat_gap)

        #         strip.setPixelColor(pix,pulse_off)
        #         print ('Off')
        #         strip.show()
        #         print(beat)
        #         time.sleep(beat)

    repeat_message = ttk.Label(dynamic_page, text='Pattern was repeated')
    repeat_message.place(x=RWidth - 6 * RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)
    dynamic_repeat_counter.append(d_repeat_counter)


def repeat_static_click():
    global s_repeat_counter, static_num_generated, beat, pix

    s_repeat_counter = s_repeat_counter + 1
    current_static_pattern = pattern_list[r_num]
    static_num_generated = True

    pix = patterns.get('pin_out')[current_static_pattern[1]][current_static_pattern[3]]
    pix_pointer = patterns.get('pin_out')[1][current_static_pattern[3]]
    print(current_static_pattern)
    print('pix = ' + str(pix))
    print('pix pointer = ' + str(pix_pointer))
    beat = 0

    # Heart beat code
    if distances[current_static_pattern[2]][0] == '10 feet':
        beat = 0.25
    elif distances[current_static_pattern[2]][0] == '15 feet':
        beat = 0.50
    elif distances[current_static_pattern[2]][0] == '20 feet':
        beat = 1.00

    print('pattern repeated')

    # # Heartbeat pattern for 10 through 20 feet
    # if ((distances[current_static_pattern[2]][0] == '20 feet') or
    #         (distances[current_static_pattern[2]][0] == '10 feet') or
    #         (distances[current_static_pattern[2]][0] == '15 feet')):
    #   strip.setPixelColor(pix_pointer,pulse_on)
    #   print ('On')
    #   strip.show()
    #   print(beat)
    #   time.sleep(1.00)

    #   strip.setPixelColor(pix_pointer,pulse_off)
    #   print ('Off')
    #   strip.show()
    #   print(beat)
    #   time.sleep(heartbeat_gap)

    #   for x in range(heartbeat_pulse):
    #         strip.setPixelColor(pix,pulse_on)
    #         print ('On')
    #         strip.show()
    #         print(beat)
    #         time.sleep(heart_gap)

    #         strip.setPixelColor(pix,pulse_off)
    #         print ('Off')
    #         strip.show()
    #         print(beat)
    #         time.sleep(heartbeat_gap)

    #         strip.setPixelColor(pix,pulse_on)
    #         print ('On')
    #         strip.show()
    #         print(beat)
    #         time.sleep(heart_gap)

    #         strip.setPixelColor(pix,pulse_off)
    #         print ('Off')
    #         strip.show()
    #         print(beat)
    #         time.sleep(beat)

    repeat_message = ttk.Label(static_page, text='Pattern was repeated')
    repeat_message.place(x=RWidth - 6 * RWidth / 7, y=RHeight - 190, anchor=tk.CENTER)


# function to deselect the elevation button
def clear_elevation_selection():
    elevation_choice.set(20)


# function to deselect the direction button
def clear_direction_selection():
    direction_choice.set(20)


# function to deselect the distance button
def clear_distance_selection():
    distance_choice.set(20)


# Create elevation Radiobuttons for familiarization page
for text, elevation in elevations:
    elevation_button = ttk.Radiobutton(familiarization_page, text=text, variable=elevation_choice, value=elevation)
    button_spacing = button_spacing + 30
    elevation_button.place(x=RWidth / 4, y=(RHeight / 4) + 5 + button_spacing, anchor=tk.CENTER)
    # create clearElevation button
clear_elevation_button = ttk.Button(familiarization_page, text='Clear', command=clear_elevation_selection)
clear_elevation_button.place(x=RWidth / 4, y=(RHeight / 4) + 5 + 120, anchor=tk.CENTER)

# Create distance Radiobuttons for familiarization page
button_spacing = 0
for text, distance in distances:
    distance_button = ttk.Radiobutton(familiarization_page, text=text, variable=distance_choice, value=distance)
    button_spacing = button_spacing + 30
    distance_button.place(x=2 * RWidth / 4, y=(RHeight / 4) + 5 + button_spacing, anchor=tk.CENTER)
# create clearDistance button
clear_distance_button = ttk.Button(familiarization_page, text='Clear', command=clear_distance_selection)
clear_distance_button.place(x=2 * RWidth / 4, y=(RHeight / 4) + 5 + 150, anchor=tk.CENTER)

# Create direction Radiobuttons for familiarization page
button_spacing = 0
for text, direction in directions:
    direct_button = ttk.Radiobutton(familiarization_page, text=text, variable=direction_choice, value=direction)
    button_spacing = button_spacing + 30
    direct_button.place(x=3 * RWidth / 4, y=(RHeight / 4) + 5 + button_spacing, anchor=tk.CENTER)
# create clearDirection button
clear_direction_button = ttk.Button(familiarization_page, text='Clear', command=clear_direction_selection)
clear_direction_button.place(x=3 * RWidth / 4, y=(RHeight / 4) + 5 + 270, anchor=tk.CENTER)

# Labels for static_page
elevation_label = ttk.Label(static_page, text='Elevation:', font=('Verdana', 15))
distance_label = ttk.Label(static_page, text='Distance:', font=('Verdana', 15))
direction_label = ttk.Label(static_page, text='Direction:', font=('Verdana', 15))

# Labels for familiarization page
elevation_label = ttk.Label(familiarization_page, text='Elevation:', font=('Verdana', 15))
distance_label = ttk.Label(familiarization_page, text='Distance:', font=('Verdana', 15))
direction_label = ttk.Label(familiarization_page, text='Direction:', font=('Verdana', 15))

# Set labels and placement
elevation_label.place(x=RWidth / 4, y=RHeight / 4, anchor='center')
distance_label.place(x=2 * RWidth / 4, y=RHeight / 4, anchor='center')
direction_label.place(x=3 * RWidth / 4, y=RHeight / 4, anchor='center')

# create Static Next button
static_next_button = ttk.Button(static_page, text='Next Static Pattern', command=next_static_click, default='active')
static_next_button.place(x=RWidth - RWidth / 7, y=RHeight - 220, anchor=tk.CENTER)
static_next_button.configure(state=tk.DISABLED)

# create Dynamic Next button
dynamic_next_button = ttk.Button(dynamic_page, text='Next Dynamic Pattern', command=next_dynamic_click,
                                 default='active')
dynamic_next_button.place(x=RWidth - RWidth / 7, y=RHeight - 220, anchor=tk.CENTER)
dynamic_next_button.configure(state=tk.DISABLED)

# create familiarization page 'Enter' button
training_next_button = ttk.Button(familiarization_page, text='Enter', command=familiarization_tab, default='active')
training_next_button.place(x=RWidth - RWidth / 7, y=RHeight - 220, anchor=tk.CENTER)

# create dynamic Save button
dynamicSaveButton = ttk.Button(dynamic_page, text='Save', command=dynamic_save_click, width=15)
dynamicSaveButton.place(x=RWidth - 2 * RWidth / 7, y=RHeight - 220, anchor=tk.CENTER)
dynamicSaveButton.configure(state=tk.DISABLED)

# create static Save button
staticSaveButton = ttk.Button(static_page, text='Save', command=static_save_click, width=15)
staticSaveButton.place(x=RWidth - 2 * RWidth / 7, y=RHeight - 220, anchor=tk.CENTER)
staticSaveButton.configure(state=tk.DISABLED)

# create dynamic restore button
restoreDynamicButton = ttk.Button(dynamic_page, text='Restore', command=restore_click, width=15)
restoreDynamicButton.place(x=RWidth - 5 * RWidth / 7, y=RHeight - 220, anchor=tk.CENTER)

# create static restore button
restoreStaticButton = ttk.Button(static_page, text='Restore', command=restore_click, width=15)
restoreStaticButton.place(x=RWidth - 5 * RWidth / 7, y=RHeight - 220, anchor=tk.CENTER)

# create dynamic repeat button
staticRepeatButton = ttk.Button(static_page, text='Repeat', command=repeat_static_click, width=15)
staticRepeatButton.place(x=RWidth - 6 * RWidth / 7, y=RHeight - 220, anchor=tk.CENTER)
staticRepeatButton.configure(state=tk.DISABLED)

# create static repeat button
dynamicRepeatButton = ttk.Button(dynamic_page, text='Repeat', command=repeat_dynamic_click, width=15)
dynamicRepeatButton.place(x=RWidth - 6 * RWidth / 7, y=RHeight - 220, anchor=tk.CENTER)
dynamicRepeatButton.configure(state=tk.DISABLED)

# create static status text
# status_message = ttk.Label(static_page, text='Status: UNSAVED')
# status_message.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=tk.CENTER)

# create dynamic status text
# status_message = ttk.Label(dynamic_page, text='Status: UNSAVED')
# status_message.place(x=RWidth - 2*RWidth/7, y=RHeight-190, anchor=tk.CENTER)

# Create NeoPixel object with appropriate configuration.
# strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Initialize the library (must be called once before other functions).
# strip.begin()

Root.mainloop()
