import numpy as np
import os.path

class IdentityMetaData:
    def __init__(self,base,name,file):
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
            metadata.append(IdentityMetaData(path, i, f))
    return np.array(metadata)

def metadata():
    metadata = load_metadata('images')
    return metadata
print(metadata())
print('Metadata Created')
