import cv2
import numpy as np
from djitellopy import tello
import time

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()
w, h = 360, 240


while True:
    #_, img = cap.read()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    cv2.imshow("Output", img)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        me.land()
        break