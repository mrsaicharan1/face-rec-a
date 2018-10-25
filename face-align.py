import cv2

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from align import AlignDlib

%matplotlib inline

def load_image(path):
    img = cv2.imread(path,1)
    return img[...,::-1] #Return in RGB instead of conventional BGR order


alignment = AlignDlib('models/landmarks.dat')
