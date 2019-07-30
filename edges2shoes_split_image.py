import matplotlib.image as mpimg
from PIL import Image
import os
import numpy as np

root = "/home/li/data/edges2shoes/train"
i=0
for item in os.listdir("/home/li/data/edges2shoes/train"):
    image = root + "/" + item
    ori_image = mpimg.imread(image)
    A_image = ori_image[0:255, 0:255, :]
    A_im = Image.fromarray(np.uint8(A_image))
    A_im.save('/home/li/data/edges2shoes/trainA/{}.jpg'.format(i))
    B_image = ori_image[0:255, 256:511, :]
    B_im = Image.fromarray(np.uint8(B_image))
    B_im.save('/home/li/data/edges2shoes/trainB/{}.jpg'.format(i))
    i=i+1
