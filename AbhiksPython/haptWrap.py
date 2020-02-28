from hapServer import *
import time

def display(distance, direction,hapserver):
    hframes = hapFrames()
    hframes.addBWFrame(waitTime,[],10)
    stripTargetRow = 6-targetRow
    waitTime = 1000

    onTime = 150
    offTime = 100

    dispList = []

    direc = int(direction/45)
    if (height == 0): 
        #round to the nearest 45 degree increment and add elements
        dispList.append(direc)

    if (height == 1): 
        #round to the nearest 45 degree increment and 15 - display
        dispList.append(15-direc)

    if (height == 2): 
        #round to the nearest 45 degree increment and display +15
        if (direc > 3):
            direc = direc + 10
        dispList.append(direc+15)




    #add elements 15+distance 25-distance
    dispList.append(20+distance)
    dispList.append(29-distance)

    hframes.addBWFrame(onTime,dispList,10)
    hframes.addBWFrame(offTime,[],10)

    hapserver.send(hframes.frames)