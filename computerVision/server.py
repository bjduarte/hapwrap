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
timeSinceLastFrame = {}


ESTIMATED_NUM_PIS = 4
ACTIVE_CHECK_PERIOD = 10
ACTIVE_CHECK_SECONDS = ESTIMATED_NUM_PIS * ACTIVE_CHECK_PERIOD

lastImages = {}

count=0

while True:
	# receive RPi name and frame from the RPi and acknowledge
	# the receipt
    (rpiName, frame) = imageHub.recv_image()
    imageHub.send_reply(b'OK')
    
    if rpiName not in lastActive.keys():
        print("[INFO] receiving data from {}...".format(rpiName))
 

    timeSinceLastFrame[rpiName] = datetime.now() - lastActive[rpiName]
    lastActive[rpiName] = datetime.now()

    cv2.imwrite("frame%d.jpg" % count, frame)
    count = count + 1

    print(rpiName + " " + str(timeSinceLastFrame[rpiName]))
    
    #depth detector
    downscaled = frame
    depth_frame=get_depth(downscaled)
    #display image

    #people detector
    persons = find_people(frame)
    #display image

    distances = {}
    directions = {}

    for person in persons:
        #calculate distance of the people
        cropped_deph_frame = depth_frame[]
        total = 0
        avg = 0
        for i in range(w):
            for j in range(h):
                total += cropped_deph_frame[i,j]

        avg = total/(w*h)

        distance = avg * unitConversion

        distances.append(distance)

        #map to a direction and add to next hap wrap update
        personOffsetPix = (person.X + (w/2)) - (frame.X/2) #centerline of the person - the center of the frame
        personOffsetDeg = (frame.X/personOffsetPix) * 90 #map pixels to degrees
        direction = personOffsetDeg + centerOffsetDeg[rpiName]

        directions.append(direction)


    #if you have newframes from every camera or its been half a second: update the hapwrap
    
    hapticFrame = {}
    #decide who to focus on
    focus = controller.read
    focusPerson = abs(directions[0]-focus)
    focusDistance = -1
    for i in range(len(directions)): #pick the closest person to the direction of focus
        if ((focusPerson-focus) < abs(directions[i] - focus):
            focusDistance = distances[i]


    #if there is a person in that direction then add to hapback display



    for i in range(len(directions)):
        intensity = distances[i]
        directions

    cv2.imshow('frame',frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()

#before
#make sure model is loaded
# download_model_if_doesnt_exist(args.model_name)
#     model_path = os.path.join("models", args.model_name)
#     print("-> Loading model from ", model_path)
#     encoder_path = os.path.join(model_path, "encoder.pth")
#     depth_decoder_path = os.path.join(model_path, "depth.pth")

#     # LOADING PRETRAINED MODEL
#     print("   Loading pretrained encoder")
#     encoder = networks.ResnetEncoder(18, False)
#     loaded_dict_enc = torch.load(encoder_path, map_location=device)

#     # extract the height and width of image that this model was trained with
#     feed_height = loaded_dict_enc['height']
#     feed_width = loaded_dict_enc['width']
#     filtered_dict_enc = {k: v for k, v in loaded_dict_enc.items() if k in encoder.state_dict()}
#     encoder.load_state_dict(filtered_dict_enc)
#     encoder.to(device)
#     encoder.eval()

#     print("   Loading pretrained decoder")
#     depth_decoder = networks.DepthDecoder(
#         num_ch_enc=encoder.num_ch_enc, scales=range(4))

#     loaded_dict = torch.load(depth_decoder_path, map_location=device)
#     depth_decoder.load_state_dict(loaded_dict)

#     depth_decoder.to(device)
#     depth_decoder.eval()

def getDepth(frame):
