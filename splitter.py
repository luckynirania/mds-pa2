import numpy as np 
import imageio
from PIL import Image as im 

def split(image_path):
    image = im.open(image_path)
    # convert image to numpy array
    data = np.asarray(image)
    print(type(data))
    print(data[:,:,0].shape)
        
    d1 = data[:,:,0]
    d2 = data[:,:,1]
    d3 = data[:,:,2]
        




    dat = im.fromarray(d1) 
    dat.save('our_data/R.png') 
    dat = im.fromarray(d2) 
    dat.save('our_data/G.png') 
    dat = im.fromarray(d3) 
    dat.save('our_data/B.png') 

split('our_data/100x100.png')

