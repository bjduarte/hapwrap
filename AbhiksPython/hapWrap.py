from hapServer import *
import time

def display2(distance, direction, elevation, hapserver):
    
    waitTime = 1000
    
    hframes = hapFrames()
    hframes.addBWFrame(waitTime,[],34)

    onTime = 150
    offTime = 100

    dispList = []

    direc = int(direction/45)
    if (elevation == 0): 
        #round to the nearest 45 degree increment and add elements
        dispList.append(direc)

    if (elevation == 1): 
        #round to the nearest 45 degree increment and 15 - display
        dispList.append(15-direc)

    if (elevation == 2): 
        #round to the nearest 45 degree increment and display +15
        if (direc > 3):
            direc = direc + 10
        dispList.append(direc+15)




    #add elements 15+distance 25-distance
    dispList.append(20+distance)
    dispList.append(29-distance)

    hframes.addBWFrame(onTime,dispList,34)
    hframes.addBWFrame(offTime,[],34)

    hapserver.send(hframes.frames)





def display(distance, direction, elevation, hapserver):
    waitTime = 1000


    hframes = hapFrames()
    hframes.addBWFrame(waitTime,[],34)
#    stripTargetRow = 6-targetRow

    onTime = 500
    offTime = 100

    dispList = []

    direc = int(direction/45)

    #bottom
    dispList.append(direc)

    #middle
    dispList.append(15-direc)

    #top
    if (direc > 3):#skip hapBack
        direc = direc + 10
    dispList.append(direc+15)



    #add elements 15+distance 25-distance
    dispList.append(20+(distance/5))
    dispList.append(29-(distance/5))

    hframes.addBWFrame(onTime,dispList,34)
    hframes.addBWFrame(offTime,[],34)

    hapserver.send(hframes.frames)