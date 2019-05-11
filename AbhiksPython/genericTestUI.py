from hapServer import *
import sys


inp = sys.argv
#inp = ["0","192.168.1.160", "10", "1000", "2","4","5"]

#on the cubic network
# backwrap 192.168.1.160
# hapwrap 192.168.1.119

serverIP = inp[1]
size = int(inp[2])
onTime = int(inp[3])
numItems = len(inp) - 4

hs = hapserver(serverIP)

hframes = hapFrames()

display = [0]*(numItems)


for i in range(numItems):
    display[i] = int(inp[i + 4])

hframes.addBWFrame(onTime,display,size)

hs.send(hframes.frames)
