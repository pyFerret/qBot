# This file is how I plan to make the robot move and 
# interact with the real world. It is for the raspberry 
# pi to be able to interact with the motors, cameras, 
# and buttons that I will attatch to make this project 
# possible. Over time I expect this file to grow quite 
# a bit, as right now all it does is start the camera 
# view. I am currently working on extracting color from 
# the camera view, so that I can see the stickers and 
# nothing else, but for the moment it just looks at 
# everything that is in frame.

import cv2
import gpiozero

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("preview")
