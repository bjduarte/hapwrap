from AbhiksPython.hapServer import hapserver
import AbhiksPython.hapBack as hb
import time
import sys

hs = hapserver()

print(sys.argv[1])
if sys.argv[1] == "1":
    hb.a1(5-int(sys.argv[2]),hs)
    time.sleep(1)

if sys.argv[1] == "2":
    hb.a2(5-int(sys.argv[2]),hs)
    time.sleep(1)

if sys.argv[1] == "3":
    hb.r1(6-int(sys.argv[2]),hs)
    time.sleep(1)

if sys.argv[1] == "4":
    hb.r2(6-int(sys.argv[2]),hs)
    time.sleep(1)
