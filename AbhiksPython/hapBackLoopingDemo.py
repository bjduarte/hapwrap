from hapServer import hapserver
import hapBack as hb
import time
import random

hs = hapserver("192.168.43.90")

while(True):
    ranLevel = random.randint(3,5)
    ranPattern = random.randint(1,4)
    print(ranLevel)
    print(ranPattern)
    if ranPattern == 1:
        hb.r1(ranLevel,hs)

    if ranPattern == 2:
        hb.r1(ranLevel,hs)

    if ranPattern == 3:
        hb.r2(ranLevel,hs)

    if ranPattern == 4:
        hb.r2(ranLevel,hs)
    time.sleep(10)
