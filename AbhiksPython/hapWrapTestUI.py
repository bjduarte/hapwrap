from hapServer import hapserver
import hapWrap as hw
import sys
ip = sys.argv[1]


hs = hapserver(ip)

while True:
    dist=input("input distance(5-25)")
    der=input("input direction(0-360)")
    hw.display(int(dist),int(der),0,hs)
