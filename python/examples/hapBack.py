from hapServer import *
import time


# diret
def a1(targetRow, hapserver):
    hframes = hapFrames()
    targetRow = 5-targetRow
    
    onTime = 500
    hframes.addBWFrame(onTime, [targetRow, 9 - targetRow], 10)

    hapserver.send(hframes.frames)


# back and forth
def a2(targetRow, hapServer):
    hframes = hapFrames()
    targetRow = 5-targetRow
    
    onTime = 200
    inBetweenTime = 100
    offTime = 200

    hframes.addBWFrame(onTime, [targetRow], 10)
    hframes.addBWFrame(inBetweenTime, [], 10)
    hframes.addBWFrame(onTime, [9 - targetRow], 10)
    hframes.addBWFrame(offTime, [], 10)
    hframes.addBWFrame(onTime, [9 - targetRow], 10)
    hframes.addBWFrame(inBetweenTime, [], 10)
    hframes.addBWFrame(onTime, [targetRow], 10)

    hapServer.send(hframes.frames)


# ladder
def r1(targetRow, hapServer):
    hframes = hapFrames()
    targetRow = 6-targetRow
    
    waitTime = 1000

    onTime = 200
    offTime = 100

    hframes.addBWFrame(waitTime, [], 10)

    for i in range(targetRow):
        hframes.addBWFrame(onTime, [i, 9 - i], 10)
        hframes.addBWFrame(offTime, [], 10)

    hapServer.send(hframes.frames)


# zig zag
def r2(targetRow, hapServer):
    hframes = hapFrames()
    targetRow = 6-targetRow
    
    waitTime = 1000

    onTime = 200
    inBetweenTime = 100
    offTime = 200

    hframes.addBWFrame(waitTime, [], 10)

    for i in range(targetRow):
        hframes.addBWFrame(onTime, [i], 10)
        #        hframes.addBWFrame(inBetweenTime,[],10)
        hframes.addBWFrame(onTime, [9 - i], 10)
    #        hframes.addBWFrame(offTime,[],10)

    # for i in range(targetRow-1,-1,-1):
    #     hframes.addBWFrame(onTime,[9-i],10)
    #     hframes.addBWFrame(inBetweenTime,[],10)
    #     hframes.addBWFrame(onTime,[i],10)
    #     hframes.addBWFrame(offTime,[],10)

    hapServer.send(hframes.frames)
