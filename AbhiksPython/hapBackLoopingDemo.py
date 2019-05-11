from hapServer import hapserver
import hapBack as hb
import time
import random

hs = hapserver("192.168.1.160")

while(True):
    ranLevel = random.randint(1,5)
    ranPattern = random.randint(1,4)
    print(ranLevel)
    print(ranPattern)
    if ranPattern == 1:
        hb.a1(ranLevel,hs)

    if ranPattern == 2:
        hb.a2(ranLevel,hs)

    if ranPattern == 3:
        hb.r1(ranLevel,hs)

    if ranPattern == 4:
        hb.r2(ranLevel,hs)
    time.sleep(10)
