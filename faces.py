import cv2
import numpy as np
from mtcnn.mtcnn import MTCNN

cam = cv2.VideoCapture(0)
detector = MTCNN()

def detect_faces(img):
    attributes = detector.detect_faces(img)
    return attributes

def xywh(img): #returns [x,y,w,h]
    img = cv2.imread(img)
    attributes = detector.detect_faces(img)
    return attributes

def webcam():
    while cam.isOpened():
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = process_frame(frame)
        cv2.imshow('frame',img)
        cv2.waitKey(1)


    cam.release()

def process_frame(img):
    rects = detector.detect_faces(img)
    # Loop through all the faces detected and determine whether or not they are in the database
    for (i,rect) in enumerate(rects):
        (x,y,w,h) = rect['box'][0],rect['box'][1],rect['box'][2],rect['box'][3]
        img = cv2.rectangle(img,(x, y),(x+w, y+h),(255,0,0),2)
    return img

if __name__=='__main__':
    webcam()
