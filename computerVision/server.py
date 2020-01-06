from imutils import build_montages
from datetime import datetime
import numpy as np
import imagezmq
import argparse
import imutils
import cv2




# initialize the ImageHub object
imageHub = imagezmq.ImageHub()
 

    # start looping over all the frames
while True:
	# receive RPi name and frame from the RPi and acknowledge
	# the receipt
    (rpiName, frame) = imageHub.recv_image()
    imageHub.send_reply(b'OK')
    

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()

