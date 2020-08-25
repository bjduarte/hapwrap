#python wrapLoop.py 192.168.43.24
from hapServerV2 import hapserver2
import hapWrap as hw
import sys
import time

ip = sys.argv[1]


hs = hapserver2(ip)

dist=0
der=0
while True:
    dist = dist + 5
    der = der + 45

    hw.display(dist%25,der%360,0,hs)
