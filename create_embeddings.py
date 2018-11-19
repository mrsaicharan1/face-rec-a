from model import create_model

nn4_small2_pretrained = create_model()


# In[2]:


nn4_small2_pretrained.load_weights('weights/nn4.small2.v1.h5')


# In[3]:


import numpy as np
import os.path

class IdentityMetadata():
    def __init__(self, base, name, file):
        # dataset base directory
        self.base = base
        # identity name
        self.name = name
        # image file name
        self.file = file

    def __repr__(self):
        return self.image_path()

    def image_path(self):
        return os.path.join(self.base, self.name, self.file) 
    
def load_metadata(path):
    metadata = []
    for i in os.listdir(path):
        for f in os.listdir(os.path.join(path, i)):
            # Check file extension. Allow only jpg/jpeg' files.
            ext = os.path.splitext(f)[1]
            if ext == '.jpg' or ext == '.jpeg' or ext=='.png':
                metadata.append(IdentityMetadata(path, i, f))
    return np.array(metadata)

metadata = load_metadata('images')
print('metadata created')
print(metadata)


# In[4]:


import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from align import AlignDlib

# get_ipython().run_line_magic('matplotlib', 'inline')

def load_image(path):
    img = cv2.imread(path, 1) #BGR
    return img[...,::-1] #RGB


alignment = AlignDlib('shape_predictor_68_face_landmarks.dat')

#combined transformation
def align_image(img):
    return alignment.align(96, img, alignment.getLargestFaceBoundingBox(img), 
                           landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)


# In[5]:


import pickle
embedded = np.zeros((metadata.shape[0], 128)) 

real_name = {}

for i, m in enumerate(metadata):
    img = load_image(m.image_path())
    img = align_image(img)
    scale RGB values to interval [0,1]
    if img is not None:
        img = (img / 255.).astype(np.float32)
        obtain embedding vector for image
        embedded[i] = nn4_small2_pretrained.predict(np.expand_dims(img, axis=0))[0]
    	real_name[os.path.dirname(m.image_path()[7:])] = embedded[i]

embeddings = open('embeddings.pkl','wb')
pickle.dump(embedded,embeddings)
embeddings.close()
