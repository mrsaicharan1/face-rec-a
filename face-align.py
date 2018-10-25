import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from align import AlignDlib

%matplotlib inline

def load_image(path):
    img = cv2.imread(path,1)
    return img[...,::-1] #Return in RGB instead of conventional BGR order


alignment = AlignDlib('models/shape_predictor_68_face_landmarks.dat')

orig = load_image(metadata[2].image_path())

bb = alignment.getLargestFaceBoundingBox(orig)

aligned = alignment.align(96, orig, bb, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)

plt.subplot(131)
plt.imshow(orig)

plt.subplot(132)
plt.imshow(orig)
plt.gca().add_patch(patches.Rectangle((bb.left(), bb.top()), bb.width(), bb.height(), fill=False, color='red'))

plt.subplot(133)
plt.imshow(aligned);
