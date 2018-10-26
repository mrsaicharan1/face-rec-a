import pandas as pd
import numpy as np
import cv2
from align_and_embeddings import load_image,align_image
from align import AlignDlib
from model import create_model
from create_metadata import metadata

metadata = metadata()
real_names = real_name()
nn4_small2_pretrained = create_model()
df1 = pd.read_pickle('./data.pickle')
df2 = pd.read_pickle('./names.pickle')
alignment = AlignDlib('shape_predictor_68_face_landmarks.dat')

def recognize(embedded):
    min_dist = 100
    _id = None
    print(real_names)
    for name,emb in real_names.items():
        dist = np.sum(np.square(emb - embedded))


        if dist < min_dist:
            min_dist = dist
            _id = name

    if min_dist > 0.56:
        return None
    else:
        print(min_dist)
        return _id







embedded = np.zeros((1, 128))


cam = cv2.VideoCapture(0)
while(True):
    ret, frame = cam.read()
    img = load_image('sai.jpg')
    img = align_image(img)
    # obtain embedding vector for image
    embedded = nn4_small2_pretrained.predict(np.expand_dims(np.array(img), axis=0))[0]
    name = recognize(embedded)
    print(name)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)


cam.release()
