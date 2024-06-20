
from hapServer import *
import time


8,9,1
7,6,5,4,3,2,1,0

#diret
def show(direction, elevation, distance, hapserver):
    hframes = hapFrames()
    stripTargetRow = 5-targetRow

    onTime = 500
    hframes.addBWFrame(onTime,[stripTargetRow, 9-stripTargetRow],10)

    hapserver.send(hframes.frames)