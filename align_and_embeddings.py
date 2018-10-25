import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from create_metadata import metadata

from align import AlignDlib

# %matplotlib inline

def load_image(path):
    img = cv2.imread(path,1)
    return img[...,::-1] #Return in RGB instead of conventional BGR order


alignment = AlignDlib('shape_predictor_68_face_landmarks.dat')


metadata = metadata()

orig = load_image(metadata[2].image_path())

bb = alignment.getLargestFaceBoundingBox(orig)

aligned = alignment.align(96, orig, bb, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)

# plt.subplot(131)
# plt.imshow(orig)
#
# plt.subplot(132)
# plt.imshow(orig)
# plt.gca().add_patch(patches.Rectangle((bb.left(), bb.top()), bb.width(), bb.height(), fill=False, color='red'))
#
# plt.subplot(133)
# plt.imshow(aligned);

def align_image(img):
    return alignment.align(96, img, alignment.getLargestFaceBoundingBox(img),landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)

embedded = np.zeros((metadata.shape[0], 128))

for i, m in enumerate(metadata):
    img = load_image(m.image_path())
    img = align_image(img)
    # scale RGB values to interval [0,1]
    img = (img / 255.).astype(np.float32)
    # obtain embedding vector for image
    embedded[i] = nn4_small2_pretrained.predict(np.expand_dims(img, axis=0))[0]

def distance(emb1, emb2):
    return np.sum(np.square(emb1 - emb2))
