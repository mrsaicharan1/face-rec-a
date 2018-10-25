from model import create_model
from utils import load_weights

nn4_small2 = create_model()

nn4_small2_weights = load_weights()

for name,w in nn4_small2_weights.items():
     if nn4_small2.get_layer(name) != None:
        nn4_small2.get_layer(name).set_weights(w)

nn4_small2.save_weights('weights/nn4.small2.v1.h5')
