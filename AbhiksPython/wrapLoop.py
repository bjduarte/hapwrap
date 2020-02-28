from hapServer import hapserver
import hapWrap as hw
import sys
import time
ip = sys.argv[1]


hs = hapserver(ip)

dist=0
der=0
while True:
    dist = dist + 5
    der = der + 45
    hw.display(dist%20,der%360,0,hs)
    time.sleep(2)