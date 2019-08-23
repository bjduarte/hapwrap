from hapServer import *
import time

def display(distance, direction):
    hframes = hapFrames()
    stripTargetRow = 6-targetRow
    waitTime = 1000

    onTime = 150
    offTime = 100

    #height == 0 
        #round to the nearest 45 degree increment and display
    #height == 2
        #round to the nearest 45 degree increment and display +15
    #height == 1 
        #round to the nearest 45 degree increment and 15 - display

    hframes.addBWFrame(waitTime,[],10)