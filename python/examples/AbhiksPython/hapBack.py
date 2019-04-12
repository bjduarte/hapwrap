from hapServer import *
import time

def a1(targetRow, hapserver):
    hframes = hapFrames()

    onTime = 500
    hframes.addBWFrame(onTime,[targetRow, 9-targetRow],10)

    hapserver.send(hframes.frames)

def a2(targetRow, hapServer):
    hframes = hapFrames()

    onTime = 200
    inBetweenTime = 100
    offTime = 200

    hframes.addBWFrame(onTime,[targetRow],10)
    hframes.addBWFrame(inBetweenTime,[],10)
    hframes.addBWFrame(onTime,[9-targetRow],10)
    hframes.addBWFrame(offTime,[],10)
    hframes.addBWFrame(onTime,[9-targetRow],10)
    hframes.addBWFrame(inBetweenTime,[],10)
    hframes.addBWFrame(onTime,[targetRow],10)


    hapServer.send(hframes.frames)


def r1(targetRow, hapServer):
    hframes = hapFrames()

    onTime = 200
    offTime = 100

    for i in range(targetRow):
        hframes.addBWFrame(onTime,[i, 9-i],10)
        hframes.addBWFrame(offTime,[],10)

    hapServer.send(hframes.frames)



def r2(targetRow, hapServer):
    hframes = hapFrames()

    onTime = 200
    inBetweenTime = 100
    offTime = 200

    for i in range(targetRow):
        hframes.addBWFrame(onTime,[i],10)
        hframes.addBWFrame(inBetweenTime,[],10)
        hframes.addBWFrame(onTime,[9-i],10)
        hframes.addBWFrame(offTime,[],10)
    
    for i in range(targetRow,-1,-1):
        hframes.addBWFrame(onTime,[9-i],10)
        hframes.addBWFrame(inBetweenTime,[],10)
        hframes.addBWFrame(onTime,[i],10)
        hframes.addBWFrame(offTime,[],10)

    hapServer.send(hframes.frames)
