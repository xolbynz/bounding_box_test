import numpy as np
import cv2
from matplotlib import pyplot as plt
import pandas as pd
import size


##화면 회전 6단계 (60도 단위 회전) (https://076923.github.io/posts/Python-opencv-6/)
def rotation(img,degree):
    img= cv2.resize(img, dsize=(640, 360), interpolation=cv2.INTER_AREA)
    height, width, channel = img.shape
    matrix = cv2.getRotationMatrix2D((width/2, height/2), degree, 0.5)
    dst = cv2.warpAffine(img, matrix, (width, height))
    plt.imshow(dst)
    plt.show()
    return dst



img0=cv2.imread('000000.png')
df0=pd.read_csv('000000.txt',sep=' ',header=None)


img1=cv2.imread('000001.png')
df1=pd.read_csv('000001.txt',sep=' ',header=None)

img2=cv2.imread('000002.png')
df2=pd.read_csv('000002.txt',sep=' ',header=None)

img3=cv2.imread('000003.png')
df3=pd.read_csv('000003.txt',sep=' ',header=None)

img4=cv2.imread('000004.png')
df4=pd.read_csv('000004.txt',sep=' ',header=None)

img5=cv2.imread('000005.png')
df5=pd.read_csv('000005.txt',sep=' ',header=None)


dst=rotation(img0,60)
dst=rotation(img1,60)
dst=rotation(img2,60)
dst=rotation(img3,60)
dst=rotation(img4,60)
dst=rotation(img5,60)