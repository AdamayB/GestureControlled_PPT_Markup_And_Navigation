import os
from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np

width, length = 1280, 720
# Put your Presentation folder name here
folderPath = "Presentation1"
#setting up webcam
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,length)
# List of presentation images
pathImages = sorted(os.listdir(folderPath), key = len)


# Hand Detection
detector = HandDetector(detectionCon=0.8,maxHands=1)

buttonCounter = 0
imgNumber = 0
gestureThreshold = 300
buttonPress = False
hs, ws = 120, 213
buttonDelay = 30 # For 30 frames won't except gesture
annotations = [[]]
annotationNumber = 0
annotationStart = False

while True:
    #import images
    #run webcam
    success, frame = cap.read()
    frame = cv2.flip(frame,1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)
    # 3D landmarks
    hands, frame = detector.findHands(frame, flipType=False)

    cv2.line(frame,(0,gestureThreshold),(width, gestureThreshold),(0,255,0),10) #The green line to mark eyes

    if hands and buttonPress == False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print(fingers)
        cx,cy = hand['center']
        lmList = hand['lmList']
        #indexFinger = lmList[8][0],lmList[8][1]
        xVal = int(np.interp(lmList[8][0], [width//2,w],[0,width]))
        yVal = int(np.interp(lmList[8][1], [150, length-150], [0, length]))
        indexFinger = xVal, yVal

        if cy <= gestureThreshold: #check to see if hand at face height
            #gesture 1 - left
            if fingers==[0,0,0,0,0]:
                print("Lefts")
                if imgNumber>0:
                    buttonPress = True
                    annotations = [[]]
                    annotationNumber = 0
                    annotationStart = False
                    imgNumber -= 1

            #gesture 2 - Right
            if fingers==[1,0,0,0,1]:
                print("Right")
                if imgNumber<len(pathImages)-1:
                    buttonPress = True
                    annotations = [[]]
                    annotationNumber = 0
                    annotationStart = False
                    imgNumber += 1
        #gesture 3 - Pointer
        if fingers == [1,1,1,0,0]:
            cv2.circle(imgCurrent, indexFinger, 12, (0,0,225),cv2.FILLED)
        #Gesture 4 - Drawing
        if fingers == [1,1,0,0,0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber+=1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 225), cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart = False
        # Gesture 5 - Erase
        if fingers == [1,1,1,1,0]:
            if annotations:
                if annotationNumber>-1:
                    annotations.pop(-1)
                    annotationNumber -= 1
                    buttonPress = True

    # To slow down the slide change speed
    if buttonPress:
        buttonCounter +=1
        if buttonCounter> buttonDelay:
            buttonCounter = 0
            buttonPress = False
    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j!=0:
                cv2.line(imgCurrent,annotations[i][j-1],annotations[i][j],(0,0,200),8)
    # WebCam on slides
    imgSmall = cv2.resize(frame,(ws, hs))
    h, w,_ = imgCurrent.shape
    imgCurrent[0:hs,w-ws:w] = imgSmall
    cv2.imshow("Slide", imgCurrent)
    cv2.imshow("Capture", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break


print("Done")
