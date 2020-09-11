import cv2 
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import rotation

##이미지 기하변형 3단계 (https://opencv-python.readthedocs.io/en/latest/doc/10.imageTransformation/imageTransformation.html)
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



def boundingbox(img,df,x이동,y이동):
    rows, cols = img.shape[:2]
    M = np.float32([[1,0,x이동],[0,1,y이동]])
    dst02 = cv2.warpAffine(img, M,(cols, rows))
    for X in range (0,len(df)):
        label=df[0][X] 
        x1=round(float(df[4][X])+x이동) 
        y1=round(float(df[5][X])+y이동)
        x2=round(float(df[6][X])+x이동)
        y2=round(float(df[7][X])+y이동)
        img2=cv2.rectangle(dst02,(x1,y1),(x2,y2),(0,255,0),1)
        img2=cv2.putText(dst02, label, (x1-10,y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
    return img2
    

img0=boundingbox(img0,df0,100,50)
img1=boundingbox(img1,df1,100,50)
img2=boundingbox(img2,df2,100,50)
img3=boundingbox(img3,df3,100,50)
img4=boundingbox(img4,df4,100,50)
img5=boundingbox(img5,df5,100,50)


def size (img):
    dst0 = cv2.resize(img, dsize=(640, 360), interpolation=cv2.INTER_AREA)
    
    return dst0


cv2.imshow('img',size(img0))
cv2.waitKey(0)

cv2.imshow('img',size(img1))
cv2.waitKey(0)

cv2.imshow('img',size(img2))
cv2.waitKey(0)

cv2.imshow('img',size(img3))
cv2.waitKey(0)

cv2.imshow('img',size(img4))
cv2.waitKey(0)
cv2.imshow('img',size(img5))
cv2.waitKey(0)
cv2.destroyAllWindows()