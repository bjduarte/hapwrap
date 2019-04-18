from hapServer import hapserver
import hapBack as hb
import time
import sys

hs = hapserver()

print(sys.argv[1])
if sys.argv[1] == "1":
    hb.a1(int(sys.argv[2]),hs)
    time.sleep(1)

if sys.argv[1] == "2":
    hb.a2(int(sys.argv[2]),hs)
    time.sleep(1)

if sys.argv[1] == "3":
    hb.r1(int(sys.argv[2]),hs)
    time.sleep(1)

if sys.argv[1] == "4":
    hb.r2(int(sys.argv[2]),hs)
    time.sleep(1)
