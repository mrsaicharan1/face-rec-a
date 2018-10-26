from mtcnn.mtcnn import MTCNN
import pandas as pd
import numpy as np
import cv2
from align_and_embeddings import img_to_encoding
from model import create_model

cam = cv2.VideoCapture(0)
detector = MTCNN()
df1 = pd.read_pickle('./data.pickle')
df2 = pd.read_pickle('./names.pickle')


def detect_faces(img):
    attributes = detector.detect_faces(img)
    return attributes

def xywh(img): #returns [x,y,w,h]
    img = cv2.imread(img)
    attributes = detector.detect_faces(img)
    return attributes

def recognize(image):
    min_dist = 100
    _id = None

    for emb in df1:
        frame_enc = img_to_encoding(image)
        dist = np.linalg.norm(emb - frame_enc)

        if dist < min_dist:
            min_dist = dist
            _id = df1.index(img)

        if min_dist > 0.52:
            return None
        else:
            return df2[_id]

def webcam():
    while cam.isOpened():
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = align(frame)
        cv2.imshow('frame',img)
        cv2.waitKey(1)


    cam.release()

def process_frame(img):
    rects = detector.detect_faces(img)
    # Loop through all the faces detected and determine whether or not they are in the database
    for (i,rect) in enumerate(rects):
        (x,y,w,h) = rect['box'][0],rect['box'][1],rect['box'][2],rect['box'][3]
        img = cv2.rectangle(img,(x, y),(x+w, y+h),(255,0,0),2)
        name = recognize(img[x:x+w,y:y+h])
        print(name)
    return img

def model_processing():
    nn4_small2_pretrained = create_model()
    nn4_small2_pretrained.load_weights('weights/nn4.small2.v1.h5')


if __name__=='__main__':
    webcam()
