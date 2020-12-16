import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def combine(zoom):
    x = np.load("our_data/R/s_vec.npy")
    x = np.transpose(x.reshape(zoom, zoom))

    y = np.load("our_data/G/s_vec.npy")
    y = np.transpose(y.reshape(zoom, zoom))

    z = np.load("our_data/B/s_vec.npy")
    z = np.transpose(z.reshape(zoom, zoom))

    rgbArray = np.zeros((zoom,zoom,3), 'uint8')
    rgbArray[..., 0] = x
    rgbArray[..., 1] = y
    rgbArray[..., 2] = z

    img = Image.fromarray(rgbArray)
    img.show()
    img.save('Reconstructed/myimg.png')
