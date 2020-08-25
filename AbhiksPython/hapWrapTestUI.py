from hapServerV2 import hapserver2
import hapWrap as hw
import sys
ip = sys.argv[1]
dist=sys.argv[2]
der=sys.argv[3]


hs2 = hapserver2(ip)


hw.display(int(dist),int(der),0,hs2)
