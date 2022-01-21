import cv2
import numpy as np


def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor()

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    cv2.imshow("Output", img)
    cv2.waitKey(1)




