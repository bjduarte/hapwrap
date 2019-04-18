from hapServer import *
import time


#diret
def a1(targetRow, hapserver):
    hframes = hapFrames()
    stripTargetRow = 5-targetRow

    onTime = 500
    hframes.addBWFrame(onTime,[stripTargetRow, 9-stripTargetRow],10)

    hapserver.send(hframes.frames)


#back and forth
def a2(targetRow, hapServer):
    hframes = hapFrames()
    stripTargetRow = 5-targetRow

    onTime = 200
    inBetweenTime = 100
    offTime = 200

    hframes.addBWFrame(onTime,[stripTargetRow],10)
#    hframes.addBWFrame(inBetweenTime,[],10)
    hframes.addBWFrame(onTime,[9-stripTargetRow],10)
#    hframes.addBWFrame(offTime,[],10)
    hframes.addBWFrame(onTime,[stripTargetRow],10)
#    hframes.addBWFrame(inBetweenTime,[],10)
    hframes.addBWFrame(onTime,[9-stripTargetRow],10)


    hapServer.send(hframes.frames)


#ladder
def r1(targetRow, hapServer):
    hframes = hapFrames()
    stripTargetRow = 6-targetRow
    waitTime = 1000

    onTime = 150
    offTime = 100

    hframes.addBWFrame(waitTime,[],10)


    for i in range(5-stripTargetRow):
        hframes.addBWFrame(onTime,[i, 9-i],10)
#        hframes.addBWFrame(offTime,[],10)

    hapServer.send(hframes.frames)


#zig zag
def r2(targetRow, hapServer):
    hframes = hapFrames()
    stripTargetRow = 6-targetRow

    waitTime = 1000

    onTime = 200
    inBetweenTime = 100
    offTime = 200

    hframes.addBWFrame(waitTime,[],10)


    for i in range(stripTargetRow):
        hframes.addBWFrame(onTime,[i],10)
#        hframes.addBWFrame(inBetweenTime,[],10)
        hframes.addBWFrame(onTime,[9-i],10)
#        hframes.addBWFrame(offTime,[],10)
    
    # for i in range(stripTargetRow-1,-1,-1):
    #     hframes.addBWFrame(onTime,[9-i],10)
    #     hframes.addBWFrame(inBetweenTime,[],10)
    #     hframes.addBWFrame(onTime,[i],10)
    #     hframes.addBWFrame(offTime,[],10)

    hapServer.send(hframes.frames)
