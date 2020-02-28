import imutils
from datetime import datetime
import numpy as np
import imagezmq
import argparse
import imutils
import cv2


imageHub = imagezmq.ImageHub()

lastActive = {}
lastActiveCheck = datetime.now()


ESTIMATED_NUM_PIS = 3
ACTIVE_CHECK_PERIOD = 10
ACTIVE_CHECK_SECONDS = ESTIMATED_NUM_PIS * ACTIVE_CHECK_PERIOD

lastDewarpedImges = {}

count=0

while True:
	# receive RPi name and frame from the RPi and acknowledge
	# the receipt
    (rpiName, frame) = imageHub.recv_image()
    imageHub.send_reply(b'OK')
    
    if rpiName not in lastActive.keys():
        print("[INFO] receiving data from {}...".format(rpiName))
 

    lastActive[rpiName] = datetime.now()

    cv2.imwrite("frame%d.jpg" % count, frame)
    count = count + 1
    #dewarpedFrame = 

    #lastDewarpedImges[rpiName] = dewarpedFrame

    print(rpiName + " " + str(frame.shape))
    
 
    #iterate over dictronary and stitch together
        #split center image and move everytong innto a list of 4 images
        #generate keyoints and merge for every set
        #have infrence run on the completed panorama

    cv2.imshow('frame',frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()

